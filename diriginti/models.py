from django.db import models


class Diriginte(models.Model):

    AOL_options = (('AOL Brasov', "AOL Brasov"), ('AOL Bucuresti', "AOL Bucuresti"),
                   ('AOL Buzau', "AOL Buzau"), ('AOL Constanta', "AOL Constanta"),
                   ('AOL Craiova', "AOL Craiova"), ('AOL Galati', "AOL Galati"),
                   ('AOL Pitesti', "AOL Pitesti"), ('AOL Ploiesti', "AOL Ploiesti"))
    nume = models.CharField(max_length=50)
    prenume = models.CharField(max_length=50)
    AOL = models.CharField(max_length=15, choices=AOL_options)
    email = models.EmailField(max_length=80)
    marca = models.IntegerField()
    activ = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nume} {self.prenume}'



