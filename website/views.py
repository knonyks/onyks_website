from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.cache import cache
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.db.models import Prefetch

import json
import time
import bleach

from .models import (
    Post,
    Member,
    ContactMessage,
    DocumentsManager,
    Project,
    ProjectImage,
    SwiperSlide,
)


# --- Strona główna z karuzelą i postami ---
def home(request):
    """Widok strony głównej z karuzelą i listą postów."""
    # Swiper respektuje Meta.ordering: ("order", "-created_at")
    swiper_images = SwiperSlide.objects.filter(is_active=True)

    # Posty respektują Meta.ordering: ("-is_pinned", "order", "-created_at")
    posts = Post.objects.all()

    # Sanitizacja treści postów (jeśli używasz cleaned_content w szablonie)
    allowed_tags = [
        "p", "br", "strong", "b", "em", "i",
        "ul", "ol", "li", "a", "blockquote", "code",
    ]
    allowed_attrs = {"a": ["href", "title", "target", "rel"]}

    for post in posts:
        post.cleaned_content = bleach.clean(
            post.content,
            tags=allowed_tags,
            attributes=allowed_attrs,
            strip=True,
        )

    return render(
        request,
        "index.html",
        {"swiper_images": swiper_images, "posts": posts},
    )


# (opcjonalnie) Jeżeli ktoś używa /index/, przekieruj na /
def index(request):
    """Przekierowanie z /index/ na stronę główną."""
    return redirect("home")


def about(request):
    """Widok strony o zespole."""
    # Member ma Meta.ordering: ("order", "name")
    members = Member.objects.all()
    return render(request, "about.html", {"members": members})


def projects(request):
    """Widok listy projektów z galeriami."""
    # Project ma Meta.ordering: ("order", "name")
    # Prefetch galerii z jawnie ustawioną kolejnością obrazków w ramach projektu
    projects_qs = Project.objects.prefetch_related(
        Prefetch(
            "gallery",
            queryset=ProjectImage.objects.order_by("order", "id"),
        )
    ).all()

    # Słownik: slug -> lista URL-i obrazków (już posortowanych)
    galleries = {
        project.slug: [
            img.get_image_url()
            for img in project.gallery.all()
            if img.get_image_url()
        ]
        for project in projects_qs
    }
    galleries_json = json.dumps(galleries, cls=DjangoJSONEncoder)

    return render(
        request,
        "projects.html",
        {"projects": projects_qs, "galleries_json": galleries_json},
    )


def documents(request):
    """Widok listy dokumentów."""
    # DocumentsManager ma Meta.ordering: ("order", "-created_at")
    documents = DocumentsManager.objects.all()
    return render(request, "documents.html", {"documents": documents})


@csrf_exempt
def live_status(request):
    if request.method == "POST":
        if len(request.body) > 100:
            return HttpResponse(b"Body too long")
        try:
            data = json.loads(request.body)
        except Exception:
            data = {}

        token = data.get("token")
        status = data.get("status")
        if token == "c26269c7-0f5d-4966-8cd5-b79acb86fb7a" and status in ("closed", "open"):
            cache.set("door_status", status, None)
            cache.set("door_time", time.time(), None)
            return HttpResponse(b"ok")
        else:
            return HttpResponse(b"Invalid parameters")
    else:
        return render(
            request,
            "live_status.html",
            {
                "door_status": cache.get("door_status", "closed"),
                "door_time": cache.get("door_time", 0),
            },
        )


def join_us(request):
    """Widok strony 'Dołącz do nas'."""
    return render(request, "join_us.html")


def contact(request):
    """Widok formularza kontaktowego, zapisujący dane i wysyłający email."""
    if request.method == "POST":
        name = request.POST.get("name") or ""
        email = request.POST.get("email") or ""
        message_text = request.POST.get("message") or ""

        # Zapisz do bazy
        ContactMessage.objects.create(
            name=name[:200],
            email=email[:254],
            message=message_text,
        )

        # (Opcjonalnie) wyślij mail – jeżeli masz skonfigurowany email backend
        try:
            if getattr(settings, "EMAIL_HOST", None):
                send_mail(
                    subject=f"Nowa wiadomość od {name}",
                    message=message_text,
                    from_email=email or getattr(settings, "DEFAULT_FROM_EMAIL", None),
                    recipient_list=["kn.onyks@gmail.com"],
                    fail_silently=True,
                )
        except Exception:
            # Nie blokuj użytkownika błędem e-maila
            pass

        messages.success(request, "Dziękujemy za wiadomość! Została zapisana.")
        return redirect("contact")

    return render(request, "contact.html")
