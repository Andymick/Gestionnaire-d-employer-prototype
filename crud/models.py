from django.db import models

#==================================================

class Employer(models.Model):
    nom = models.CharField(max_length=20)
    numero = models.CharField(max_length=10)
    email = models.EmailField()
    poste = models.CharField(max_length=20)
