document.addEventListener("DOMContentLoaded", function () {
  // Inicjalizacja Swiper
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

  // Animacja kart
  const cards = document.querySelectorAll(".card");
  console.log("Cards found:", cards.length);

  const observer = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const index = Array.from(cards).indexOf(entry.target);
          console.log(
            `Animating card ${index} from ${index % 2 === 0 ? "left" : "right"}`
          );

          if (index % 2 === 0) {
            entry.target.classList.add("show-left");
          } else {
            entry.target.classList.add("show-right");
          }

          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.3 }
  );

  cards.forEach((card) => {
    observer.observe(card);
  });
});
