# Generated by Django 2.1.5 on 2019-02-16 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumestc', '0003_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='img',
            field=models.ImageField(default='can1.jpg', upload_to=''),
        ),
    ]
