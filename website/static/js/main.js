document.addEventListener("DOMContentLoaded", function () {
  // === MENU (z zabezpieczeniem, gdy elementów nie ma) ===
  const menuIcon = document.getElementById("menu-icon");
  const navLinks = document.getElementById("nav-links");
  if (menuIcon && navLinks) {
    menuIcon.addEventListener("click", function () {
      navLinks.classList.toggle("show");
    });
  }

  // === SWIPER: auto-wybór selektora (.swiper preferowane, fallback .swiper-container) ===
  const swiperSelector = document.querySelector(".swiper")
    ? ".swiper"
    : (document.querySelector(".swiper-container") ? ".swiper-container" : null);

  let swiper = null;
  if (swiperSelector) {
    try {
      swiper = new Swiper(swiperSelector, {
        loop: true,
        pagination: { el: ".swiper-pagination", clickable: true },
        navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
        autoplay: { delay: 3000, disableOnInteraction: false },
        // Przydatne, gdy slajdy mają różne wysokości/rozmiary:
        observeParents: true,
        observer: true,
      });

      // Jeśli obrazy ładują się po czasie — po "load" zrób update
      window.addEventListener("load", () => {
        try { swiper.update(); } catch (_) {}
      });

      // Diagnostyka: brak slajdów / zero wysokości kontenera
      const wrapper = document.querySelector(`${swiperSelector} .swiper-wrapper`);
      if (!wrapper || wrapper.children.length === 0) {
        console.warn("[Swiper] Brak slajdów w .swiper-wrapper (sprawdź context 'swiper_images').");
      }
      const containerEl = document.querySelector(swiperSelector);
      if (containerEl && containerEl.clientHeight === 0) {
        console.warn("[Swiper] Wysokość kontenera = 0 (sprawdź CSS: .swiper {height: ...}).");
      }
    } catch (e) {
      console.error("[Swiper] Inicjalizacja nieudana:", e);
    }
  } else {
    console.warn("[Swiper] Nie znaleziono kontenera .swiper ani .swiper-container.");
  }

  // === ANIMACJA KART (z zabezpieczeniem) ===
  const cards = document.querySelectorAll(".card");
  if (cards.length) {
    const observer = new IntersectionObserver(
      (entries, obs) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const index = Array.from(cards).indexOf(entry.target);
          entry.target.classList.add(index % 2 === 0 ? "show-left" : "show-right");
          obs.unobserve(entry.target);
        });
      },
      { threshold: 0.3 }
    );
    cards.forEach((card) => observer.observe(card));
  }
});
