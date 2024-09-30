from django.db import models

# Create your models here.

class Home(models.Model):
    email = models.CharField(max_length= 300)
    date = models.DateField()

    def __str__(self):
        return self.email
    

