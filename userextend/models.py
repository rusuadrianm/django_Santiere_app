from django.contrib.auth.models import User
from django.db import models


class ProfilUser(models.Model):
    my_user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='img/')
    descriere = models.TextField()
    tip_user = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return f'{self.my_user.first_name} {self.my_user.last_name}'

