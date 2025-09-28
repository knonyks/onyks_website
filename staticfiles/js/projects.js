$(document).ready(function () {
  const menuIcon = document.getElementById("menu-icon");
  const navLinks = document.getElementById("nav-links");

  if (menuIcon && navLinks) {
    menuIcon.addEventListener("click", function () {
      navLinks.classList.toggle("show");
      console.log("Menu icon clicked, toggling 'show' class.");
    });
  }

  function showGallery(projectKey) {
    if (typeof galleries === "undefined") {
      console.error("Zmienna 'galleries' nie została zdefiniowana.");
      return;
    }

    const images = galleries[projectKey];

    if (!images || images.length === 0) {
      console.warn("Brak galerii dla projektu:", projectKey);
      return;
    }

    // Wyczyść poprzednią zawartość
    $("#galleryContent").empty();

    // Dodaj nowe obrazy
    images.forEach(function (src) {
      $("#galleryContent").append(
        `<div><img src="${src}" alt="Gallery Image" /></div>`
      );
    });

    // Inicjalizacja slick tylko raz
    if ($("#galleryContent").hasClass("slick-initialized")) {
      $("#galleryContent").slick("unslick");
    }

    $("#galleryContent").slick({
      infinite: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: true,
      dots: true,
      adaptiveHeight: true,
      centerMode: true,
      centerPadding: "0px",
    });

    $("#galleryOverlay").css("display", "flex");
  }

  $(".project img").on("click", function () {
    if (window.innerWidth > 1230) {
      const projectKey = $(this).closest(".project").data("movie");
      showGallery(projectKey);
    }
  });

  $(".project img").on("dblclick", function () {
    if (window.innerWidth <= 1230) {
      const projectKey = $(this).closest(".project").data("movie");
      showGallery(projectKey);
    }
  });

  // Zamykanie galerii przycisk „X”
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
