from django import forms
from .models import Vastaus

class VastausForm(forms.ModelForm):
    class Meta:
        model = Vastaus
        fields = [
            'nimimerkki', 'tyytyvaisyys', 'stressi', 'ahdistus', 'esimiestuki', 'tyokaverituki', 'tunnustus', 'yhteiso', 'ilo', 'palaute'
        ]
        widgets = {
            'nimimerkki': forms.TextInput(attrs={'class': 'form-control'}),
            'tyytyvaisyys': forms.Select(choices=[(i, i) for i in range(1, 11)] + [('', 'En halua vastata')], attrs={'class': 'form-control'}),
            'stressi': forms.Select(choices=[(i, i) for i in range(1, 11)] + [('', 'En halua vastata')], attrs={'class': 'form-control'}),
            'ahdistus': forms.Select(choices=[(i, i) for i in range(1, 11)] + [('', 'En halua vastata')], attrs={'class': 'form-control'}),
            'esimiestuki': forms.Select(choices=[(i, i) for i in range(1, 11)] + [('', 'En halua vastata')], attrs={'class': 'form-control'}),
            'tyokaverituki': forms.Select(choices=[(i, i) for i in range(1, 11)] + [('', 'En halua vastata')], attrs={'class': 'form-control'}),
            'tunnustus': forms.Select(choices=[(i, i) for i in range(1, 11)] + [('', 'En halua vastata')], attrs={'class': 'form-control'}),
            'yhteiso': forms.Select(choices=[(i, i) for i in range(1, 11)] + [('', 'En halua vastata')], attrs={'class': 'form-control'}),
            'ilo': forms.Select(choices=[(i, i) for i in range(1, 11)] + [('', 'En halua vastata')], attrs={'class': 'form-control'}),
            'palaute': forms.Textarea(attrs={'class': 'form-control'}),
        }
