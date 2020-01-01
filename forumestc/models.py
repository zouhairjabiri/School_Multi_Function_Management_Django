from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class theme(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Departement(models.Model):
    Code_filiere = models.CharField(max_length=30, unique=True)
    departement  = models.CharField(max_length=80)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.Code_filiere


class Subject(models.Model):
    themedis = models.ForeignKey(theme, on_delete=models.CASCADE, related_name='theme')
    subject = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    valider = models.IntegerField(default=0)

    def __str__(self):
        return self.subject  


class Reponse(models.Model):
    Reponse = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='Reponse')
    valider = models.IntegerField(default=0)

    def __str__(self):
        return self.Reponse


class utilisateur(models.Model):
    # Les Champs Oblige De Le Remplir
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Code_apogee = models.CharField(max_length=8, default=0)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    CIN = models.CharField(max_length=10)
    Filiere = models.CharField(max_length=80, default=0)
    cne = models.CharField(max_length=10)
    img = models.ImageField(default='can1.jpg')
    complete = models.IntegerField(default=0)
    active = models.IntegerField(default=0)

    def __str__(self):
        return self.User.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        utilisateur.objects.create(User=instance)
    instance.utilisateur.save()