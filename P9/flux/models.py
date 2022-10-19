from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models
from six import python_2_unicode_compatible
from PIL import Image


@python_2_unicode_compatible
class Ticket(models.Model):
    title = models.fields.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.fields.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (200, 200)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        # sauvegarde de l’image redimensionnée dans le système de fichiers
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

        def __str__(self):
            return f'{self.title}'


@python_2_unicode_compatible
class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


@python_2_unicode_compatible
class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user',)
