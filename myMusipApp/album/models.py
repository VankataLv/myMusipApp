from django.core.validators import MinValueValidator
from django.db import models

from myMusipApp.profiles.models import Profile


class Album(models.Model):
    GENRE_CHOICES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    )

    album_name = models.CharField(
        null=False, blank=False,
        unique=True,
        max_length=30,
    )
    artist_name = models.CharField(
        null=False, blank=False,
        max_length=30,
    )
    genre = models.CharField(
        null=False, blank=False,
        max_length=30,
        choices=GENRE_CHOICES
    )
    description = models.TextField(
        null=True, blank=True,
    )
    image_url = models.URLField(
        null=False, blank=False,
    )
    price = models.FloatField(
        null=False, blank=False,
        validators=[MinValueValidator(0.0),]
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
