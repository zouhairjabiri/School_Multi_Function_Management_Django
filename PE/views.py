from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from forumestc.models import Departement
from tablib import Dataset
from django.core.files.storage import FileSystemStorage


def index(request):
    titre = 'EST CASABLANCA'
    actualiteslist1 = actualité.objects.all().order_by('date').reverse()
    actualiteslist2 = actualité.objects.filter(id__gt=0).order_by('date')
    annonceslist1 = annonce.objects.all().order_by('date').reverse()
    return render(request, 'PE/index.html', {'titre': titre, 'actualiteslist1': actualiteslist1,'actualiteslist2': actualiteslist2, 'annonceslist1': annonceslist1})
        

def motdudirecteur(request):
    titre = 'Mot Du Directeur'
    return render(request, 'PE/motdudirecteur.html', {'titre': titre})



def evenements(request):
    titre = 'Evenements'
    evenements = evenement.objects.all().order_by('date').reverse()
    return render(request, 'PE/evenements.html', {'titre': titre, 'evenements': evenements})



def addevent(request):
    titre = 'Evenements'
    if request.method == 'POST':
        titre = request.POST.get('titre')
        lieu = request.POST.get('lieu')
        Description = request.POST.get('description')
        club_recup = request.POST.get('club')
        club_id = club.objects.get(club=club_recup).id
        print(club_recup)
        print(club_id)
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        evenement.objects.create(titre=titre, lieu=lieu, description=Description,img=filename,club=club(club_id))
        return redirect('plateformetudiant:evenements')
    else:
        return redirect('plateformetudiant:evenements')
    return redirect('plateformetudiant:evenements')



def test(request):
    titre = 'test'
    return render(request, 'PE/test.html', {'titre': titre})


def vote(request):
    candidats = candidat_president.objects.all()
    titre = "Les elections de L'ecole"
    return render(request, 'PE/vote.html', {'titre': titre, 'candidats': candidats})


def vote_candidat(request, pk):
    candidat = candidat_president.objects.get(id=pk)
    Departements = Departement.objects.all()
    titre = candidat.candidat_allname
    return render(request, 'PE/voteprofile.html', {'titre': titre, 'candidat': candidat, 'Departements': Departements})


def addvote(request, pk):
    if request.method == 'POST':
        name = request.POST.get('electeur_allname')
        cin = request.POST.get('electeur_cin')
        candidat = candidat_president.objects.get(id=pk).id
        if etudiant.objects.filter(CIN = cin).exists():
            electeur.objects.create(electeur_allname=name, electeur_cin=cin, candidat=candidat_president(candidat))
            upvote = candidat_president.objects.get(id=pk).candidat_totalvote
            upvote = upvote+1
            candidat_president.objects.filter(id=candidat).update(candidat_totalvote=upvote) 
        return redirect('plateformetudiant:vote')
    else:
        return redirect('plateformetudiant:vote')



def admineventlogin(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('plateformetudiant:adminevent')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('plateformetudiant:adminevent')
    else:
        form = AuthenticationForm()
    return render(request, 'PE/admineventlogin.html', {'form': form})


def adminevent(request):
    if request.user.is_superuser or request.user.is_staff:
        clubs = club.objects.all()
        return render(request, 'PE/adminevent.html', {'clubs':clubs})
    else: 
        return redirect('plateformetudiant:evenements')

