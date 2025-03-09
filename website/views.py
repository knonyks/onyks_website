from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def projects(request):
    return render(request, "projects.html")

def contact(request):
    return render(request, "contact.html")

def live_status(request):
    return render(request, "live_status.html")

def join_us(request):
    return render(request, "join_us.html")

from django.shortcuts import render

def about(request):
    members = [
        {
            "name": "Mateusz Turycz",
            "position": "Prezes",
            "image": "images/profiles/mateusz.png",
            "description": "Jeden z odrodzicieli obecnej generacji koła. Człowiek orkiestra...",
            "specialties": ["Python", "CAD 3D", "Altium Designer", "Drony", "Drukarki 3D"],
            "facebook": "https://www.facebook.com/profile.php?id=100014090220701",
            "github": "https://github.com/TH3Mateo",
            "linkedin": "https://www.linkedin.com/in/mateusz-turycz-668396264/"
        },
        {
            "name": "Szymon Bartosik",
            "position": "Sekretarz",
            "image": "images/profiles/szymon.png",
            "description": "Zwolennik porządku i dokładności, wytrawny elektronik...",
            "specialties": ["C", "AVR", "RF", "SolidEdge"],
            "facebook": "https://www.facebook.com/profile.php?id=100017236899585",
            "github": "https://github.com/xJacksee",
            "linkedin": "https://www.linkedin.com/in/szymon-bartosik-578249281/"
        },
        {
            "name": "Janusz Stepanik",
            "position": "Skarbnik",
            "image": "images/profiles/janusz.png",
            "description": "Weteran WEiTI. Doskonały przewodnik dla nowych członków...",
            "specialties": ["STM32", "Python"],
            "facebook": "https://www.facebook.com/profile.php?id=100009501830846",
            "github": "https://github.com/JohhnyLat",
            "linkedin": "https://www.linkedin.com/in/janusz-stepanik/"
        },
        {
            "name": "Bartosz Mruk",
            "position": "Zastępca skarbnika",
            "image": "images/profiles/bartosz.png",
            "description": "Murarz, tynkarz, akrobata. Zawsze świadczy szybką pomocą...",
            "specialties": ["(Arch) Linux", "Matematyka"],
            "facebook": "https://www.facebook.com/share/18LBgNztPQ/",
            "github": "https://github.com/BRM42795"
        },
        {
            "name": "Rafał Chojnacki",
            "position": "Administrator mediów",
            "image": "images/profiles/rafal.png",
            "description": "Zawsze działa za kulisami i planuje przejąć władzę w tym kole...",
            "specialties": ["Python", "JavaScript", "WWW"],
            "github": "https://github.com/RafalCho02",
            "linkedin": "https://www.linkedin.com/in/rafa%C5%82-chojnacki-540441253/"
        }
    ]
    return render(request, "about.html", {"members": members})

from django.shortcuts import render

def projects(request):
    projects = [
        {
            "id": "project1",
            "name": "Drukarka 3D ONYKSON",
            "image": "images/projects/drukarka_3d_onykson/drukarka1.png",
            "description": "Bazując na projekcie open source drukarki Voron 2, projektujemy naszą własną konstrukcję..."
        },
        {
            "id": "project2",
            "name": "Monitoring pomieszczeń IoT",
            "image": "images/projects/monitoring_iot/iot1.png",
            "description": "Projekt ONYKS IoT to praktyczna inicjatywa rozwijająca umiejętności projektowania elektroniki..."
        },
        {
            "id": "project3",
            "name": "Narzędzia z włókna węglowego",
            "image": "images/projects/narzedzia_karbon/karbon1.png",
            "description": "Stosując formy zaprojektowane w CAD 3D i wydrukowane na drukarkach 3D, tworzymy własne narzędzia..."
        }
    ]
    return render(request, "projects.html", {"projects": projects})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Wysyłanie maila (konfiguracja w settings.py)
        send_mail(
            f"Nowa wiadomość od {name}",
            message,
            email,
            ["kn.onyks@gmail.com"],
            fail_silently=False,
        )

        messages.success(request, "Twoja wiadomość została wysłana!")
    
    return render(request, "contact.html")