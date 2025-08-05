from django.core.mail import send_mail
from django.contrib import messages


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
            "description": "Jeden z odrodzicieli obecnej generacji koła. Człowiek orkiestra, wysłannik chaosu, wyznawca szybkich drukarek 3D i pilot dronów.",
            "specialties": ["Python", "CAD 3D", "Altium Designer", "Drony", "Drukarki 3D"],
            "facebook": "https://www.facebook.com/profile.php?id=100014090220701",
            "github": "https://github.com/TH3Mateo",
            "linkedin": "https://www.linkedin.com/in/mateusz-turycz-668396264/"
        },
        {
            "name": "Szymon Bartosik",
            "position": "Sekretarz",
            "image": "images/profiles/szymon.png",
            "description": "Zwolennik porządku i dokładności, wytrawny elektronik i mikrofalowiec. Nadaje organizacji profesjonalizmu. Włada rejestrami mikrokontrolerów i potężną matematyką.
  Fan elektorniki analogowej i mikrokontrolerów AVR (za Ar***no wyrzuca z koła)",

            "specialties": ["C", "AVR", "RF", "SolidEdge"],
            "facebook": "https://www.facebook.com/profile.php?id=100017236899585",
            "github": "https://github.com/xJacksee",
            "linkedin": "https://www.linkedin.com/in/szymon-bartosik-578249281/"
        },
        {
            "name": "Janusz Stepanik",
            "position": "Zastępca Skarbnik",
            "image": "images/profiles/janusz.png",
            "description": "Weteran WEiTI. Doskonały przewdonik dla nowych człownków.
Znawca tranzystorów mocy i strażnik lodówki. Specjalista od prania pieniędzy i biurokracji.",

            "specialties": ["STM32", "Python"],
            "facebook": "https://www.facebook.com/profile.php?id=100009501830846",
            "github": "https://github.com/JohhnyLat",
            "linkedin": "https://www.linkedin.com/in/janusz-stepanik/"
        },
        {
            "name": "Bartosz Mruk",
            "position": "Skarbnik",
            "image": "images/profiles/bartosz.png",
"description": "Murarz, tynkarz, akrobata. Zawsze świadczy szybką pomocą przy kwestiach organizacyjnych. Doskonały dawca pomysłów na niekonwencjonalne rozwiązania techniczne. Zdał Metody Numeryczne za pierwszym razem.
Tak swoją drogą to używa Arch Linuxa.",

            "specialties": ["(Arch) Linux", "Matematyka"],
            "facebook": "https://www.facebook.com/share/18LBgNztPQ/",
            "github": "https://github.com/BRM42795"
        },
        {
            "name": "Rafał Chojnacki",
            "position": "Administrator mediów",
            "image": "images/profiles/rafal.png",
            "description": "Zawsze działa za kulisami i planuje przejąć władzę w tym kole. Programista Python i Web Dev. Zawodowo zajmuje się automatyką, a z powołania zgłębia tajniki historii. Zawsze wygra z Tobą w Geoguesser.",
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
            "description": """Bazując na projekcie open source drukarki Voron 2, projektujemy naszą własną konstrukcję, której motywem przewodnim jest niski koszt materiałów i łatwość obsługi.
Staramy się uzyskać dużą powierzchnię roboczą przy możliwie najmniejszej liczbie elementów, tak aby nasza drukarka była "surowym" szkieletem gotowym na bardziej
zaawansowane ulepszenia. Drukarka opiera się na systemie "Core XY"."""
        },
        {
            "id": "project2",
            "name": "Monitoring pomieszczeń IoT",
            "image": "images/projects/monitoring_iot/iot1.png",
            "description": """Projekt ONYKS IoT to praktyczna inicjatywa, która stawia na rozwijanie umiejętności z projektowania elektroniki i programowania systemów wbudowanych - od systemów monitoringu drzwi, aż po narzędzia do inwentaryzacji urządzeń. 
Każdy może spróbować swoich sił w projektowaniu sprzętu czy programowaniu. Pracujemy nad realnymi rozwiązaniami, które można zastosować np. w laboratoriach, salach zajęciowych czy innych Kołach."""
        },
        {
            "id": "project3",
            "name": "Narzędzia z włókna węglowego",
            "image": "images/projects/narzedzia_karbon/karbon1.png",
            "description": """Stosując formy zaprojektowane przez nas w CAD 3D i wydrukowane na drukarkach 3D staramy się tworzyć własne narzędzia z włókna węglowego spojonego żywicą.
Planujemy produkować narzędzia takie jak pensety, które są często używane w warsztacie elektronika."""
        }
    ]
    return render(request, "projects.html", {"projects": projects})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            f"Nowa wiadomość od {name}",
            message,
            email,
            ["kn.onyks@gmail.com"],
            fail_silently=False,
        )
        messages.success(request, "Twoja wiadomość została wysłana!")

    return render(request, "contact.html")

def live_status(request):
    return render(request, "live_status.html")

def join_us(request):

    return render(request, "join_us.html")


