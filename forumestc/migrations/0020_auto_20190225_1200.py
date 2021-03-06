# Generated by Django 2.1.5 on 2019-02-25 12:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0019_auto_20190225_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='Departement',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='utilisateur_cin',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='CIN',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='Code_apogee',
            field=models.CharField(default=0, max_length=8),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='Filiere',
            field=models.CharField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='cne',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='nom',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='prenom',
            field=models.CharField(max_length=15),
        ),
    ]
