from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Max

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Możesz używać HTML do formatowania tekstu.")
    created_at = models.DateTimeField(auto_now_add=True)
    is_pinned = models.BooleanField("Przypięty", default=False)
    order = models.PositiveIntegerField("Kolejność (gdy przypięty)", default=0)

    class Meta:
        # Najpierw posty przypięte wg order, reszta chronologicznie
        ordering = ['-is_pinned', 'order', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-nadanie kolejności tylko gdy przypięty i order=0
        if self.is_pinned and (self.order is None or self.order == 0):
            max_order = Post.objects.filter(is_pinned=True).aggregate(m=Max('order'))['m'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)


class Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/profiles/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="Zewnętrzny link do obrazka (priorytetowy nad plikiem)")
    description = models.TextField()
    specialties = models.CharField(max_length=300)
    facebook = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField("Kolejność", default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def get_specialties_list(self):
        return [s.strip() for s in self.specialties.split(',') if s.strip()]

    def get_avatar_url(self):
        return self.image_url if self.image_url else (self.image.url if self.image else None)

    def save(self, *args, **kwargs):
        if self.order is None or self.order == 0:
            max_order = Member.objects.aggregate(m=Max('order'))['m'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField("Kolejność", default=0)

    class Meta:
        ordering = ['order', 'name']

    @property
    def get_thumbnail(self):
        if self.thumbnail_url:
            return self.thumbnail_url
        elif self.image:
            return self.image.url
        else:
            return ""

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.order is None or self.order == 0:
            max_order = Project.objects.aggregate(m=Max('order'))['m'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="gallery")
    image = models.ImageField(upload_to="images/projects/", blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    link_target = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField("Kolejność w projekcie", default=0)

    class Meta:
        ordering = ['order', 'id']
        unique_together = [('project', 'order')]  # jedna kolejność w obrębie projektu

    def __str__(self):
        src = self.image.name if self.image else self.image_url
        return f"{self.project.name} - {src}"

    def get_image_url(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return ""

    def save(self, *args, **kwargs):
        # Auto-kolejność w ramach projektu
        if self.order is None or self.order == 0:
            max_order = ProjectImage.objects.filter(project=self.project).aggregate(m=Max('order'))['m'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']  # w panelu i widokach najnowsze na górze

    def __str__(self):
        return f"{self.name} ({self.email})"


class DocumentsManager(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    drive_url = models.URLField("Link do pliku na Google Drive")
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField("Kolejność", default=0)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if self.order is None or self.order == 0:
            max_order = DocumentsManager.objects.aggregate(m=Max('order'))['m'] or 0
            self.order = max_order + 1
        super().save(*args, **kwargs)


class SwiperSlide(models.Model):
    title = models.CharField("Tytuł/ALT", max_length=200, blank=True)
    image_file = models.ImageField("Plik lokalny", upload_to="swiper/", blank=True, null=True)
    image_url = models.URLField("Adres URL obrazu", blank=True)
    order = models.PositiveIntegerField("Kolejność", default=0)
    is_active = models.BooleanField("Aktywny", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Swiper Slide"
        verbose_name_plural = "Swiper Slides"

    def __str__(self):
        return self.title or f"Slajd #{self.pk}"

    def clean(self):
        super().clean()
        if not self.image_file and not self.image_url:
            raise ValidationError("Podaj URL obrazu lub wgraj plik.")

    @property
    def image_src(self) -> str:
        if self.image_file:
            return self.image_file.url
        return self.image_url
