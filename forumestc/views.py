from django.shortcuts import render, redirect
from forumestc.models import *
from PE.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from django.core.files.storage import FileSystemStorage


def index(request):
    titre = 'forum'
    themes = theme.objects.all().order_by('name')
    compte_id=request.user.id
    compte = 0
    if request.user.is_active:
        compte=utilisateur.objects.get(User=compte_id)
    if request.user.is_superuser or request.user.is_staff:
        return redirect('forumestc:administrateur')
    else:
        return render(request, 'forumestc/forum.html', {'themes': themes, "titre": titre, 'compte':compte})


def forum2(request, pk):
    sujet = Subject.objects.filter(themedis=pk)
    dpt = Subject.objects.filter(themedis=pk)
    return render(request, 'forumestc/forum2.html', {'sujet': sujet, 'dpt': dpt})


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('forumestc:forum_home')
    else:
        form = UserCreationForm()
    return render(request, 'forumestc/include/sign_up.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('forumestc:forum_home')
    else:
        form = AuthenticationForm()
    return render(request, 'forumestc/include/log_in.html', {'form': form})



def log_out(request):
    if request.method == 'POST':
        if request.user.is_superuser:
            logout(request)
            return redirect('forumestc:forum_home')
        else:
            logout(request)
            return redirect('forumestc:forum_home')


def moncompte(request, pk):
    compte_id=request.user.id
    compte=utilisateur.objects.get(User=compte_id)
    compte2 = 0
    if compte.complete == 1:
        cin_compte=compte.CIN
        compte2=etudiant.objects.get(CIN=cin_compte)
    return render(request, 'forumestc/include/moncompte.html',{'compte':compte,'compte2':compte2})


def sujet(request, pk):
    themec = theme.objects.get(id=pk)
    sujets = Subject.objects.filter(themedis=pk)
    themec_id = themec.id
    return render(request, 'forumestc/sujets.html', {'sujets': sujets, 'themec': themec, 'themec_id': themec_id})


def reponse(request, pk):
    dpt = Subject.objects.get(id=pk).themedis
    sujetc = Subject.objects.get(id=pk)
    sujet_id = Subject.objects.get(id=pk).id
    reponses = Reponse.objects.filter(Subject=pk)
    return render(request, 'forumestc/reponses.html', {'reponses': reponses, 'sujetc':sujetc,'dpt':dpt, 'sujet_id':sujet_id})


def validersujet(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        sujetv = Subject.objects.get(id=pk)
        sujetv.valider=1
        sujetv.save()
        return redirect('forumestc:administrateur')
    else:
        return redirect('forumestc:forum_home')


def supprsujet(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        sujetv = Subject.objects.get(id=pk)
        sujetv.delete()
        return redirect('forumestc:administrateur')
    else:
        return redirect('forumestc:forum_home')


def addsubject(request, dpt_id):
    if request.method == 'POST':
        subject = request.POST.get('sujet')
        Subject.objects.create(subject=subject, themedis=theme(dpt_id))
        return redirect('forumestc:forum_home')
    else:
        return render(request, 'forumestc/sujets.html')


def addreponse(request, sujet_id):
    if request.method == 'POST':
        reponse = request.POST.get('sujet')
        Reponse.objects.create(Reponse=reponse, Subject=Subject(sujet_id))
        return redirect('forumestc:forum_home')
    else:
        return render(request, 'forumestc/sujets.html')


def validerreponse(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        reponsev = Reponse.objects.get(id=pk)
        reponsev.valider=1
        reponsev.save()
        return redirect('forumestc:administrateur')
    else:
        return redirect('forumestc:forum_home')


def supprreponse(request, pk):
    if request.user.is_superuser or request.user.is_staff:
        reponsev = Reponse.objects.get(id=pk)
        reponsev.delete()
        return redirect('forumestc:administrateur')
    else:
        return redirect('forumestc:forum_home')


def moncompteupdate(request, pk):
    compte_id=request.user.id
    compte=User.objects.get(id=compte_id)

    if request.method == 'POST':
        CIN = request.POST.get('CIN')
        CNE = request.POST.get('CNE')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        #Departement = request.POST.get('Departement')
        #annedenaissance = request.POST.get('annedenaissance')
        utilisateur.objects.filter(User=compte_id).update(  
        CIN = CIN,
        cne = CNE,
        complete = 1,
        img=filename
        )
        return redirect('forumestc:forum_home')
    else:
        return redirect('forumestc:forum_home')



def administrateur(request):
    if request.user.is_superuser or request.user.is_staff:
        titre = 'Espace administrateur du forum ESTC'
        sujets = Subject.objects.all()
        reponses = Reponse.objects.all()
        return render(request, 'forumestc/administrateur.html', {'titre': titre, 'sujets': sujets, 'reponses': reponses})
    else:
        return redirect('forumestc:forum_home')



