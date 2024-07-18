from django.shortcuts import render
from .models import Haber

def anasayfa(request):
    son_haberler = Haber.objects.all().order_by('-yayinlanma_tarihi')[:15]
    return render(request, 'haberler/anasayfa.html', {'son_haberler': son_haberler})
