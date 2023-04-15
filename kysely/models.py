from django.db import models
from django.utils import timezone
# Create your models here.
class Vastaus(models.Model):
    nimimerkki = models.CharField(max_length=100)
    tyytyvaisyys = models.IntegerField(blank=True, null=True)
    stressi = models.IntegerField(blank=True, null=True)
    ahdistus = models.IntegerField(blank=True, null=True)
    esimiestuki = models.IntegerField(blank=True, null=True)
    tyokaverituki = models.IntegerField(blank=True, null=True)
    tunnustus = models.IntegerField(blank=True, null=True)
    yhteiso = models.IntegerField(blank=True, null=True)
    ilo = models.IntegerField(blank=True, null=True)
    palaute = models.TextField(blank=True)
    aikaleima = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nimimerkki
