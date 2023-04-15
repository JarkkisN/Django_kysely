from django.contrib import admin
from .models import Vastaus

class VastausAdmin(admin.ModelAdmin):
    list_display = ('nimimerkki', 'tyytyvaisyys', 'stressi', 'ahdistus', 'esimiestuki', 'tyokaverituki', 'tunnustus', 'yhteiso', 'ilo', 'palaute', 'aikaleima')

admin.site.register(Vastaus)
