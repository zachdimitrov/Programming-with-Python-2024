from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    age = models.IntegerField(validators=[MinValueValidator(16), MaxValueValidator(99)])
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField(validators=MaxLengthValidator(200))
    count = models.SmallIntegerField()
    positive_count = models.PositiveIntegerField()
    real_number = models.FloatField()
    decimal_number = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)