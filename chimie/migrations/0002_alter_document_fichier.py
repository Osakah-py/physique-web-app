# Generated by Django 3.2.9 on 2023-02-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chimie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='fichier',
            field=models.FileField(upload_to='static/pdf/chimie'),
        ),
    ]
