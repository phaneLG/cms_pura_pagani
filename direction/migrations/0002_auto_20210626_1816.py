# Generated by Django 3.2.4 on 2021-06-26 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depense',
            name='date_debut',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='date_debut',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='date_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personnel',
            name='date_naissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recette',
            name='date_debut',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recette',
            name='date_fin',
            field=models.DateField(blank=True, null=True),
        ),
    ]
