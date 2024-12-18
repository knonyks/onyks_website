document.addEventListener("DOMContentLoaded", function () {
  // Obsługa menu
  const menuIcon = document.getElementById("menu-icon");
  const navLinks = document.getElementById("nav-links");

  menuIcon.addEventListener("click", function () {
    navLinks.classList.toggle("show");
    console.log("Menu icon clicked, toggling 'show' class.");
  });

  // Animacja kart podczas przewijania
  const cards = document.querySelectorAll(".card");
  
  // Dodaj logowanie, aby sprawdzić, czy karty zostały znalezione
  console.log("Cards found:", cards.length);

  const observer = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const index = Array.from(cards).indexOf(entry.target);
          
          console.log(`Animating card ${index} from ${index % 2 === 0 ? "left" : "right"}`);
          
          // Naprzemienne przypisywanie klas `show-left` i `show-right`
          if (index % 2 === 0) {
            entry.target.classList.add("show-left");
          } else {
            entry.target.classList.add("show-right");
          }
          
          observer.unobserve(entry.target); // Przestajemy obserwować po dodaniu animacji
        }
      });
    },
    {
      threshold: 0.3, // Widoczność na 30%
    }
  );

  cards.forEach((card) => {
    observer.observe(card);
  });
});
