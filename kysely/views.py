from django.shortcuts import render
from .forms import VastausForm

def kysely_view(request):
    if request.method == 'POST':
        form = VastausForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'kysely/kiitos.html')
    else:
        form = VastausForm()
    return render(request, 'kysely/kysely.html', {'form': form})
