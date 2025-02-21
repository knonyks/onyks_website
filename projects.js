$(document).ready(function () {
    const menuIcon = document.getElementById("menu-icon");
    const navLinks = document.getElementById("nav-links");
  
    menuIcon.addEventListener("click", function () {
      navLinks.classList.toggle("show");
      console.log("Menu icon clicked, toggling 'show' class.");
    });
    
    const galleries = {
        "project1": [
            "images/projects/drukarka_3d_onykson/drukarka1.png",
            "images/projects/drukarka_3d_onykson/drukarka2.png",
            "images/projects/drukarka_3d_onykson/drukarka3.png",
            "images/projects/drukarka_3d_onykson/drukarka4.png"
        ],
        "project2": [
            "images/projects/monitoring_iot/iot1.png",
            "images/projects/monitoring_iot/iot2.png",
            "images/projects/monitoring_iot/iot3.png",
            "images/projects/monitoring_iot/iot4.png"
        ],
        "project3": [
            "images/projects/narzedzia_karbon/karbon1.png",
            "images/projects/narzedzia_karbon/karbon2.png",
            "images/projects/narzedzia_karbon/karbon3.png"
        ]
    };

    function showGallery(projectKey) {
        const images = galleries[projectKey];

        if (images) {
            $("#galleryContent").empty();
            
            images.forEach(function (src) {
                $("#galleryContent").append(`<div><img src="${src}" alt="Gallery Image" /></div>`);
            });

            $("#galleryContent").slick({
                infinite: true,
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: true,
                dots: true,
                adaptiveHeight: true,
                centerMode: true,
                centerPadding: '0px'
            });

            $("#galleryOverlay").css("display", "flex");
        }
    }

    $(".project img").on("click", function () {
        if (window.innerWidth > 1230) { // Sprawdź, czy szerokość okna jest większa niż 768px
            const projectKey = $(this).closest(".project").data("movie"); // Użyj 'data-movie'
            showGallery(projectKey);
        }
    });

    $(".project img").on("dblclick", function () {
        if (window.innerWidth <= 1230) { // Sprawdź, czy szerokość okna jest mniejsza lub równa 768px
            const projectKey = $(this).closest(".project").data("movie"); 
            showGallery(projectKey);
        }
    });

    // Zamykanie galerii po kliknięciu przycisku zamknięcia
    $("#closeGallery").on("click", function () {
        $("#galleryOverlay").css("display", "none"); 
        if ($("#galleryContent").hasClass("slick-initialized")) {
            $("#galleryContent").slick("unslick"); 
        }
    });

    // Zamykanie galerii po kliknięciu w tło
    $("#galleryOverlay").on("click", function (e) {
        if (e.target === this) {
            $(this).css("display", "none"); 
            if ($("#galleryContent").hasClass("slick-initialized")) {
                $("#galleryContent").slick("unslick");
            }
        }
    });
});
