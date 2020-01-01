from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(evenement, club, actualité, electeur, annonce, etudianttest)
class ViewAdmin(ImportExportModelAdmin):
    pass


class etudiantadmin(admin.ModelAdmin):
	list_display = ('Code_apogee','nom', 'prenom','Filiere','CIN', 'cne')
	list_filter = ('Filiere', 'complete')
	search_fields = ('Code_apogee','nom', 'prenom','Filiere','CIN', 'cne')
	ordering = ('nom', 'prenom')

class candidatadmin(admin.ModelAdmin):
	list_display = ('candidat_allname','candidat_totalvote','candidat_departement')
	list_filter = ('candidat_totalvote',)
	ordering = ('candidat_totalvote','candidat_allname')

admin.site.register(candidat_president, candidatadmin)
admin.site.register(etudiant, etudiantadmin)