from django.db import models
from forumestc.models import *
from django.utils import timezone



# *** TABLE actualité ********************************************************************

class actualité(models.Model):
    titre = models.CharField(max_length=100)
    image = models.ImageField(default='default.png')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


# *** TABLE annonce ********************************************************************

class annonce(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre



# *** TABLE club ********************************************************************
class club(models.Model):
    club = models.CharField(max_length=40)

    def __str__(self):
        return self.club


# *** TABLE evenement ********************************************************************
class evenement(models.Model):
    titre = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    img = models.ImageField(default='default.png')
    lieu = models.CharField(max_length=50)
    club = models.ForeignKey(club, on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(default='defaultText')

    def __str__(self):
        return self.titre


# *** TABLE elecetion ********************************************************************
class candidat_president(models.Model):
    candidat_allname = models.CharField(max_length=40)
    candidat_departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    candidat_totalvote = models.IntegerField(default=0)
    candidat_img = models.ImageField()

    def __str__(self):
        return self.candidat_allname


# *** TABLE electeur********************************************************************
class electeur(models.Model):
    electeur_allname = models.CharField(max_length=40)
    electeur_cin = models.CharField(max_length=50, unique=1)
    candidat = models.ForeignKey(candidat_president, on_delete=models.CASCADE)

    def __str__(self):
        return self.electeur_allname

# *** TABLE anonypme********************************************************************

class etudiant(models.Model):
    Code_apogee = models.CharField(max_length=8, default=0)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    CIN = models.CharField(max_length=10)
    Filiere = models.CharField(max_length=80, default=0)
    cne = models.CharField(max_length=10)
    # Les Champs Optionnel De Le Remplir
    #img = models.ImageField(default='can1.jpg')
    #email = models.CharField(max_length=10, default='email')    
    #annedenaissance = models.DateField(default=now)
    complete = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

# *** TABLE anonypme********************************************************************

class etudianttest(models.Model):
    Code_apogee = models.CharField(max_length=8, default=0)
    nom = models.CharField(max_length=15)
    prenom = models.CharField(max_length=15)
    CIN = models.CharField(max_length=10)
    Filiere = models.CharField(max_length=80, default=0)
    cne = models.CharField(max_length=10)
    # Les Champs Optionnel De Le Remplir
    #img = models.ImageField(default='can1.jpg')
    #email = models.CharField(max_length=10, default='email')    
    #annedenaissance = models.DateField(default=now)
    complete = models.IntegerField(default=0)

    def __str__(self):
        return self.nom
