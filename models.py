from django.db import models

# Create your models here.
class veh(models.Model):
    speed = models.IntegerField()
    avgSpeed = models.IntegerField()
    temperature = models.FloatField()
    fuelLevel = models.FloatField()
    EngineStatus = models.TextField(max_length=30)
    cam1 = models.TextField(max_length=5)
    cam2 = models.TextField(max_length=5)
