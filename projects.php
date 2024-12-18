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
        <img src="images\gallery\image1.jpeg" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Projekt</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Recusandae iure rerum unde, dolore id assumenda repudiandae quam cum labore quos sunt necessitatibus voluptate laborum sed harum enim voluptatem. Consectetur saepe tempore blanditiis hic fuga quos neque voluptatum eligendi suscipit distinctio. At reprehenderit nulla voluptates facilis a fuga modi ullam rerum, voluptatibus officiis distinctio eveniet autem reiciendis quo vel voluptatem eius laboriosam illo, nisi mollitia. Iste cumque illo alias minima explicabo..</p>
        </div>
      </div>
      <div class="project" data-movie="project2">
        <img src="images\gallery\image2.jpg" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Projekt</h3>
          <p>Opis Projekt  1.</p>
        </div>
      </div>
      <div class="project" data-movie="project3">
        <img src="images\gallery\image3.jpg" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Projekt</h3>
          <p>Opis Projekt  1.</p>
        </div>
      </div>
      <div class="project" data-movie="project3">
        <img src="images\gallery\image4.jpg" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Projekt</h3>
          <p>Opis Projekt  1.</p>
        </div>
      </div>
      <div class="project" data-movie="project3">
        <img src="images\gallery\image4.jpg" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Projekt</h3>
          <p>Opis Projekt  1.</p>
        </div>
      </div>
      <div class="project" data-movie="project3">
        <img src="images\gallery\image4.jpg" alt="Zdjęcie projektu" />
        <div class="overview">
          <h3>Projekt</h3>
          <p>Opis Projekt  1.</p>
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
