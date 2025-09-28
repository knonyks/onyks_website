from django import forms
from django.contrib import admin
from django.utils.html import format_html

from .models import (
    ContactMessage,
    DocumentsManager,
    Member,
    Post,
    Project,
    ProjectImage,
    SwiperSlide,
)


# ====== POST ======

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "content": forms.Textarea(attrs={"rows": 15, "cols": 100}),
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ("title", "is_pinned", "order", "created_at")
    list_editable = ("is_pinned", "order")
    ordering = ("-is_pinned", "order", "-created_at")
    search_fields = ("title", "content")


# ====== MEMBER ======

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "order")
    list_editable = ("order",)
    ordering = ("order", "name")
    search_fields = ("name", "position", "specialties")
    fields = (
        "name",
        "position",
        "description",
        "specialties",
        "image",
        "image_url",
        "facebook",
        "github",
        "linkedin",
        "order",
    )


# ====== PROJECT & IMAGES ======

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 0
    fields = ("image", "image_url", "link_target", "order")
    ordering = ("order", "id")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
    list_editable = ("order",)
    ordering = ("order", "name")
    prepopulated_fields = {"slug": ("name",)}
    fields = ("name", "description", "image", "thumbnail_url", "slug", "order")
    inlines = [ProjectImageInline]
    search_fields = ("name", "description")


# ====== CONTACT MESSAGES ======

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at")
    ordering = ("-submitted_at",)
    search_fields = ("name", "email", "message")


# ====== DOCUMENTS ======

@admin.register(DocumentsManager)
class DocumentsManagerAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "created_at")
    list_editable = ("order",)
    ordering = ("order", "-created_at")
    search_fields = ("title", "description")


# ====== SWIPER SLIDE ======

@admin.register(SwiperSlide)
class SwiperSlideAdmin(admin.ModelAdmin):
    list_display = ("thumb", "title", "order", "is_active", "created_at")
    list_editable = ("order", "is_active")
    search_fields = ("title",)
    ordering = ("order", "-created_at")
    fieldsets = (
        (None, {"fields": ("title", "is_active", "order")}),
        ("Obraz", {"fields": ("image_file", "image_url")}),
    )

    def thumb(self, obj):
        src = obj.image_src if obj.pk else ""
        if not src:
            return "—"
        return format_html(
            '<img src="{}" style="height:60px;border-radius:6px;" />', src
        )

    thumb.short_description = "Podgląd"
