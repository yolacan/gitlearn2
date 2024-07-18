from django.db import models

class Haber(models.Model):
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    yayinlanma_tarihi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.baslik
