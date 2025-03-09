from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),  # Strona główna
    path("about/", views.about, name="about"),  # O nas
    path("projects/", views.projects, name="projects"),  # Projekty
    path("contact/", views.contact, name="contact"),  # Kontakt
    path("live_status/", views.live_status, name="live_status"),  # Live status
    path("join_us/", views.join_us, name="join_us"),  # Dołącz do nas
]
