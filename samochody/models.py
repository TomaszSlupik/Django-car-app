from django.db import models

class Samochody (models.Model):

    marka = models.CharField(max_length=20)
    zdjecie =models.ImageField(upload_to='zdjecia', null=True, blank=True)
    opis = models.TextField(default="")
    salon = models.ImageField(upload_to='zdjecia', null=True, blank=True)


