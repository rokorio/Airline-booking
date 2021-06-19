from django.db import models

# Create your models here.


# Create your models here.
class Airport(models.Model):
    code=models.CharField(max_length=3,primary_key=True,unique=True)
    city=models.CharField(max_length=72,unique=True)


    def __str__(self):
        return f"{self.city} ({self.code})"

class Flights(models.Model):
    origin1=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departures')
    destination2=models.ForeignKey(Airport,on_delete=models.CASCADE,related_name='departures')
    duration3=models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

