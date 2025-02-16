from django.db import models

class Citizen(models.Model):
    
    CITIES = [
        ('Sf', 'Sofia'),
        ('Pd', 'Plovdiv'),
        ('Bs', 'Burgas'),
        ('Vn', 'Varna'),
    ]

    # correct way for choises
    class Cities(models.TextChoices):
        SF = 'Sf', 'Sofia'
        PD = 'Pd', 'Plovtiv'
        BS = 'Bs', 'Burgas'
        VN = 'Vn', 'Varna'

    first_name = models.CharField(max_length=50)
    age = models.IntegerField() 
    # PositiveIntegerField
    # FloatField() - bez garantirana tochnost
    # DecimalField() - s golqma tochnost
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50, choise=CITIES)
    description = models.TextField()
    birth = models.DateField()
    # TimeField() 
    # DateTimeField()
    ## arguments - auto_now=True - zapazva se za vsqka promqna
    ## auto_now_add=True - zapisva samo vednaj
    married = models.BooleanField()
    web_site = models.URLField() # max length = 200 default
    email = models.EmailField() # max length = 254 default
    
    '''
    other arguments:

    null=True
    blank=True
    default=10
    primary_key=True
    unique=True - false by default
    choise=CITIES
    '''

    def __str__(self):
        return  self.name

