from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name= models.CharField(max_length=300)
    last_name= models.CharField(max_length=400)
    instrument= models.CharField(max_length=100)
    
    def __str__(self) -> str:
         return self.first_name 
#     + '' + self.last_name + ''+self.instrument
    
    class Album(models.Model):
          name = models.CharField(max_length=100)
          release_date = models.DateField()
          num_stars = models.IntegerField()
