# website/urls.py
from django.urls import path
from .views import home, index, about, projects, documents, contact, join_us, live_status

urlpatterns = [
    path("", home, name="home"),          
    path("index/", index, name="index"),
    path("about/", about, name="about"),
    path("projects/", projects, name="projects"),
    path("documents/", documents, name="documents"),
    path("contact/", contact, name="contact"),
    path("join-us/", join_us, name="join_us"),
    path("live-status/", live_status, name="live_status"),
    path('admin/', admin.site.urls),
]
