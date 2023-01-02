# Generated by Django 3.2.9 on 2023-01-02 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrap', '0002_rename_documents_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='categorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scrap.categorie'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='description',
            field=models.TextField(default=' '),
        ),
    ]
