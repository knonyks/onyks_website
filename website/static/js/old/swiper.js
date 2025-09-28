document.addEventListener("DOMContentLoaded", function () {
  // --- SWIPER: wybór selektora zgodnie z HTML/CSS (nowe .swiper lub starsze .swiper-container)
  const swiperSelector = document.querySelector(".swiper")
    ? ".swiper"
    : (document.querySelector(".swiper-container") ? ".swiper-container" : null);

  let swiper = null;

  if (swiperSelector && typeof Swiper !== "undefined") {
    try {
      swiper = new Swiper(swiperSelector, {
        loop: true,
        pagination: { el: ".swiper-pagination", clickable: true },
        navigation: { nextEl: ".swiper-button-next", prevEl: ".swiper-button-prev" },
        autoplay: { delay: 3000, disableOnInteraction: false },
        observer: true,
        observeParents: true,
      });

      // Gdy obrazy doładują się po czasie – zaktualizuj układ
      const container = document.querySelector(swiperSelector);
      const imgs = container ? container.querySelectorAll("img") : [];
      let pending = imgs.length;
      if (pending > 0) {
        imgs.forEach(img => {
          if (img.complete) {
            pending -= 1;
          } else {
            img.addEventListener("load", () => {
              if (swiper) swiper.update();
            }, { once: true });
            img.addEventListener("error", () => {
              if (swiper) swiper.update();
            }, { once: true });
          }
        });
        if (pending === 0 && swiper) swiper.update();
      }

      // Awaryjnie po pełnym załadowaniu strony
      window.addEventListener("load", () => { if (swiper) swiper.update(); });
    } catch (e) {
      console.error("[Swiper] Błąd inicjalizacji:", e);
    }
  } else {
    console.warn("[Swiper] Nie znaleziono kontenera (.swiper / .swiper-container) lub brak Swipera.");
  }

  // --- ANIMACJA KART ---
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
