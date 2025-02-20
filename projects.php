<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Onyx</title>
        <link rel="stylesheet" href="styles.css" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick-theme.css"/>
        <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
        integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
        crossorigin="anonymous"
      />
  
        <link rel="icon" href="images/ico.ico" type="image/png">
    
        <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js"></script>
      </head>
  <body>
    <?php include 'header.php'; ?>

    <section class="projects">
      <div class="project" data-movie="project1">
        <img src="images/projects/drukarka_3d_onykson/drukarka1.png" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Drukarka 3D ONYKSON</h3>
          <p>Bazując na projekcie open source drukarki Voron 2, projektujemy naszą własną konstrukcję, której motywem przewodnim jest niski koszt materiałów i łatwość obsługi.
            Staramy się uzyskać dużą powierzchnię roboczą przy możliwie najmniejszej liczbie elementów, tak aby nasza drukarka była "surowym" szkieletem gotowym na bardziej
            zaawansowane ulepszenia. Drukarka opiera się na systemie "Core XY".
          </p>
        </div>
      </div>
      <div class="project" data-movie="project2">
        <img src="images/projects/monitoring_iot/iot1.png" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Monitoring pomieszczeń IoT</h3>
          <p>Projekt ONYKS IoT to praktyczna inicjatywa, która stawia na rozwijanie umiejętności z projektowania elektroniki i programowania systemów wbudowanych - od systemów monitoringu drzwi, aż po narzędzia do inwentaryzacji urządzeń. 
          Każdy może spróbować swoich sił w projektowaniu sprzętu czy programowaniu. Pracujemy nad realnymi rozwiązaniami, które można zastosować np. w laboratoriach, salach zajęciowych czy innych Kołach. </p>
        </div>
      </div>
      <div class="project" data-movie="project3">
        <img src="images/projects/narzedzia_karbon/karbon1.png" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Narzędzia z włókna węglowego</h3>
          <p>Stosując formy zaprojektowane przez nas w CAD 3D i wydrukowane na drukarkach 3D staramy się tworzyć własne narzędzia z włókna węglowego spojonego żywicą.
            Planujemy produkować narzędzia takie jak pensety, które są często używane w warsztacie elektronika.
          </p>
        </div>
      </div>

      <!-- Nakładka galerii -->
      <div id="galleryOverlay" class="gallery-overlay">
        <span id="closeGallery" class="close-gallery">&times;</span>
        <div id="galleryContent" class="gallery-content slider">
          <!-- Obrazy galerii będą dodawane dynamicznie przez JavaScript -->
        </div>
      </div>
    </section>


    </section>
    <?php include 'footer.php'; ?>
    
    
    <script src="projects.js"></script>
  </body>
</html>
