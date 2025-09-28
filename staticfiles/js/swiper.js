document.addEventListener("DOMContentLoaded", function () {
  const menuIcon = document.getElementById("menu-icon");
  const navUl = document.querySelector(".nav ul");

  console.log(navUl); // sprawdzenie elementu

  // Domyślne ustawienie
  let state = false;

  function updateMenuDisplay() {
    if (window.innerWidth > 1230) {
      navUl.style.display = "flex";
    } else if (state === false) {
      navUl.style.display = "none";
    }
  }

  // Ustaw początkowy stan
  updateMenuDisplay();

  menuIcon.addEventListener("click", function () {
    if (navUl.style.display === "none" || navUl.style.display === "") {
      navUl.style.display = "flex";
      console.log("dupa");
      state = true;
    } else {
      navUl.style.display = "none";
      state = false;
    }
  });

  // Reakcja na zmianę rozmiaru okna
  window.addEventListener("resize", updateMenuDisplay);

  // Konfiguracja Swiper – przeniesiona *do środka* DOMContentLoaded
  const swiper = new Swiper(".swiper-container", {
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
  });
}); // <-- tylko jedno zamknięcie!
