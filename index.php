<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="styles.css" />
    <link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css" />
    <script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
    <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
    integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
    crossorigin="anonymous"
  />
    <title>Onyx</title>
    <link rel="icon" href="images/ico.ico" type="image/png">

    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
  </head>
  <body>
  <?php include 'header.php'; ?>
    <div class="hero">
      <div class="swiper-container">
        <div class="swiper-wrapper">
          <div class="swiper-slide">
            <img src="images\gallery\1735335298398.jpg" alt="Zdjęcie 1" />
          </div>
          <div class="swiper-slide">
            <img src="images\gallery\IMG_20241207_140841.jpg" alt="Zdjęcie 2" />
          </div>
          <div class="swiper-slide">
            <img src="images\gallery\1735335298463.jpg" alt="Zdjęcie 3" />
          </div>
          <div class="swiper-slide">
            <img src="images\gallery\1735335298487.jpg" alt="Zdjęcie 4" />
          </div>
          <div class="swiper-slide">
            <img src="images\gallery\462557519_2492981804229890_4379326778538732516_n.jpg" alt="Zdjęcie 5" />
          </div>
          <div class="swiper-slide">
            <img src="images\gallery\IMG_20241004_211342.jpg" alt="Zdjęcie 6" />
          </div>
        </div>
        <!-- Dodaj nawigację Swiper -->
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
        <div class="swiper-pagination"></div>
      </div>
    
      <!-- Przyciemnienie -->
      <div class="overlay"></div>
    
      <!-- Warstwa tekstowa -->
      <div class="text-layer">
        <h1>Witamy na stronie Koła Mikrosystemów ONYKS!</h1>
        <p>Lutownica w dłoń! </br> Dołącz do imperium pasjonatów elektroniki</p>
      </div>
    </div>
    
    </div>

    <section class="container content">
      <h2>Czym jest ONYKS?</h2>
      <p>
        ONYKS to organizacja studencka działająca na wydziale Elektroniki i Technik Informacyjnych Politechniki Warszawskiej. 
        Koło Naukowe powstało  w celu wspólnego realizowania projektów elektronicznych i wzjamenego wymieniania się wiedzą i doświadczeniami.
        ONYKS to ludzie chcący dzielić się pasją do tworzenia urządzeń i rozwijania istniejących rozwiązań.
        Nie teoria a praktyka zrobią z Ciebie elektryka!
      </p>

      <h3>Dlaczego warto do nas dołączyć?</h3>
      <p>
        <ul class="content">
          <li>Poznasz ludzi o podobnych zainteresowaniach</li>
          <li>Uczestnicząc w projektach zdobędziesz praktyczne doświadczenie</li>
          <li>Otrzymasz pomoc w realizacji własnych projektów</li>
          <li>Będziesz miał okazję uczestniczyć w hackathonach w zespole razem z nami</li>
          <li>Zyskasz dostęp do profesjonalnego warsztatu i materiałów</li>
        </ul>
      </p>
      <h3>Kogo potrzebujemy?</h3>
      <p>
        Zachęcamy do dołączenia wszystkich pasjonatów elektroniki i technologii. 
        W szczegówlności zależy nam na osobach zajmujących się:
        <ul class="content">
          <li>Produkcją własnych PCB</li>
          <li>Programowaniem FPGA i CPLD</li>
          <li>Projektowaniem układów i PCB</li>
          <li>Programowaniem mikrokontrolerów AVR, ARM i RISC-V</li>
          <li>Modelowaniem w CAD 3D</li>
      </p>
    </section>
    <?php include 'footer.php'; ?>
    <script src="swiper.js"></script>
  </body>
</html>
