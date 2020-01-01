from django.urls import path
from . import views

app_name = 'forumestc'

urlpatterns = [
    path('', views.index, name='forum_home'),
    path('forum2/<int:pk>', views.forum2, name='forum2'),
    path('administrateur/', views.administrateur, name='administrateur'),

    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('moncompte/<int:pk>', views.moncompte, name='moncompte'),
    path('moncompteupdate/<int:pk>', views.moncompteupdate, name='moncompteupdate'),

    path('sujet/<int:pk>', views.sujet, name='sujet'),
    path('reponse/<int:pk>', views.reponse, name='reponse'),


    path('addsubject/<int:dpt_id>', views.addsubject, name='addsubject'),
    path('validersujet/<int:pk>', views.validersujet, name='validersujet'),
    path('supprsujet/<int:pk>', views.supprsujet, name='supprsujet'),

    
    path('addreponse/<int:sujet_id>', views.addreponse, name='addreponse'),
    path('validerreponse/<int:pk>', views.validerreponse, name='validerreponse'),
    path('supprreponse/<int:pk>', views.supprreponse, name='supprreponse'),



]
