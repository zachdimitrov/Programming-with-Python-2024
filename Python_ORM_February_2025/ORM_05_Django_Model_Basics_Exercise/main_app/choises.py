from django.db import models

class GenreChoises(models.TextChoices):
    FICTION = "Fn", "Fiction"
    NON_FICTION = "Nf", "Non-Fiction"
    SCIENCE_FICTION = "Sf", "Science Fiction"
    HORROR = "Hr", "Horror"