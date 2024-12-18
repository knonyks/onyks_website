<?php
      $currentPage = basename($_SERVER['PHP_SELF'], ".php");
    ?>
    <nav class="nav">
      <div class="container">
        <img class="logo" src="images/logo.png" alt="Logo">
        <h1 class="wut-info">Koło Naukowe Mikrosystemów <br><p>Politechnika Warszawska</p></h1>
        <div class="menu-icon" id="menu-icon">
          <i class="fas fa-bars"></i>
        </div>
        <ul class="nav-links" id="nav-links">
          <li><a href="index.php" class="<?= $currentPage == 'index' ? 'current' : '' ?>">Home</a></li>
          <li><a href="about.php" class="<?= $currentPage == 'about' ? 'current' : '' ?>">O nas</a></li>
          <li><a href="projects.php" class="<?= $currentPage == 'projects' ? 'current' : '' ?>">Projekty</a></li>
          <li><a href="contact.php" class="<?= $currentPage == 'contact' ? 'current' : '' ?>">Kontakt</a></li>
          <li><a href="live_status.php" class="<?= $currentPage == 'live_status' ? 'current' : '' ?>">Live status</a></li>
          <li><a href="join_us.php" class="<?= $currentPage == 'join_us' ? 'current' : '' ?>">Dołącz do nas</a></li>
        </ul>
      </div>
    </nav>

    <script src="swiper.js"></script>