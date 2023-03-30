from django.db import models

from diriginti.models import Diriginte


class Santier(models.Model):

    tipuri_santier = (
        ('bransament', 'Bransament'), ('extindere', 'Extindere'),
        ('deviere', 'Deviere'), ('sistematizare', 'Sistematizare'),
        ('reabilitare', 'Reabilitare'), ('redimensionare', 'Redimensionare')
    )

    statusuri = (('amanat', 'amanat'), ('in lucru', 'in lucru'), ('executat', 'executat'), ('sistat', 'sistat'), (' ',"--"))

    data = models.DateField()
    tip_santier = models.CharField(max_length=15, choices=tipuri_santier)
    localitate = models.CharField(max_length=25)
    strada = models.CharField(max_length=40)
    numar = models.CharField(max_length=10, null=True)
    tip_lucrari = models.CharField(max_length=25)
    constructor = models.CharField(max_length=40)
    SDA = models.CharField(max_length=13)

    diriginte = models.ForeignKey(Diriginte, on_delete=models.CASCADE, null=True)

    numar_aparitie =models.IntegerField(null=True)
    status = models.CharField(max_length=10, choices=statusuri, default='--')
    observatie = models.CharField(max_length=150, null=True)
    nota = models.IntegerField(null=True)

    poza1 = models.ImageField(upload_to='img/', null=True)
    poza2 = models.ImageField(upload_to='img/', null=True)
    poza3 = models.ImageField(upload_to='img/', null=True)
    are_poza = models.CharField(max_length=3, null=True, default="Nu")

    solicitare =models.FileField(upload_to='file/solicitari/', null=True)
    document = models.FileField(upload_to='file/alte_doc/', null=True)
    vizita = models.FileField (upload_to='file/vizite/', null=True)
    are_vizita = models.CharField(max_length=3, null=True, default="Nu")


    def __str__(self):
        return f'{self.data} - {self.localitate}, {self.strada} {self.numar} ({self.constructor})'
