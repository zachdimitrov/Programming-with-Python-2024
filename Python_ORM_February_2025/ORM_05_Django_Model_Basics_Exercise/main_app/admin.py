from django.contrib import admin
from main_app.models import Book, Exercise, Product

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass