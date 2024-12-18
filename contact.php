<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="stylesheet" href="styles.css" />
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

    <section class="about">
      <div class="contact-wrapper">
          
          <!-- Informacje kontaktowe -->
          <div class="contact-details-box">
              <h3>Nasza siedziba</h3>
              <p><i class="fas fa-building"></i> <strong>Koło Naukowe Mikrosystemów</strong></p>
              <p><i class="fas fa-map-marker-alt"></i> <strong>Adres:</strong> ul. Nowowiejska 15, 00-665 Warszawa, Polska</p>
              <p><i class="fas fa-envelope"></i> <strong>Email:</strong> <a href="mailto:kontakt@kolo-mikrosystemow.pl">kontakt@kolo-mikrosystemow.pl</a></p>
              <p><i class="fas fa-phone"></i> <strong>Numer telefonu:</strong> +48 123 456 789</p>
          </div>
          
          <!-- Formularz kontaktowy -->
          <div class="contact-form-box">
              <h3>Skontaktuj się z nami</h3>
              <form class="contact-form" action="#" method="post">
                  <div class="form-group">
                      <label for="name"><i class="fas fa-user"></i> Imię i nazwisko</label>
                      <input type="text" id="name" name="name" placeholder="Twoje imię i nazwisko" required>
                  </div>
  
                  <div class="form-group">
                      <label for="email"><i class="fas fa-envelope"></i> Email</label>
                      <input type="email" id="email" name="email" placeholder="Twój adres email" required>
                  </div>
  
                  <div class="form-group">
                      <label for="message"><i class="fas fa-comment"></i> Wiadomość</label>
                      <textarea id="message" name="message" rows="5" placeholder="Twoja wiadomość" required></textarea>
                  </div>
  
                  <button type="submit"><i class="fas fa-paper-plane"></i> Wyślij</button>
              </form>
          </div>
          
      </div>
  
      <!-- Mapa Google -->
      <div class="map-container">
          <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2443.439716761322!2d21.007139415802203!3d52.2204967797598!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x471ecc6cfc82b97d%3A0x4f2a4c3e05dfac41!2sPolitechnika%20Warszawska!5e0!3m2!1spl!2spl!4v1603195073519!5m2!1spl!2spl"
              width="100%" height="600" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
      </div>
  </section>
  
  
  
  
  
  
  <?php include 'footer.php'; ?>
    
    
    <script src="script.js"></script>
  </body>
</html>
