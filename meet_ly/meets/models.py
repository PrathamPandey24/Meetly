from django.db import models

# Create your models here.
class Meet(models.Model):
    Place=models.CharField(max_length=100)
    date=models.DateField()
    time=models.TimeField()
    Client_name = models.CharField(max_length=100)
    Description = models.TextField()


    def __str__(self):
        return self.Place