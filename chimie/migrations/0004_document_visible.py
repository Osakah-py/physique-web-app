# Generated by Django 3.2.9 on 2024-07-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chimie', '0003_alter_document_fichier'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]