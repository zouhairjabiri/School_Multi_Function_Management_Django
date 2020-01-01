from django.urls import path, include

from . import views

app_name = 'plateformetudiant'


urlpatterns = [
	path('', views.index, name='home'),
	path('', include('forumestc.urls'), name='forum_home'),
	path('motdudirecteur/', views.motdudirecteur, name='motdudirecteur'),
	path('evenements/', views.evenements, name='evenements'),
	path('test/', views.test, name='test'),
	path('vote/', views.vote, name='vote'),
	path('vote_candidat/<int:pk>', views.vote_candidat, name='vote_candidat'),
    path('addvote/<int:pk>', views.addvote, name='addvote'),
    path('admineventlogin/', views.admineventlogin, name='admineventlogin'),
    path('adminevent/', views.adminevent, name='adminevent'),
    path('addevent/', views.addevent, name='addevent'),
]