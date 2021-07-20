# Generated by Django 3.2.4 on 2021-06-26 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(blank=True)),
                ('date_fin', models.DateField(blank=True)),
                ('laboratoire', models.FloatField(blank=True, null=True)),
                ('autre_achat', models.FloatField(blank=True, null=True)),
                ('medicament', models.FloatField(blank=True, null=True)),
                ('menage', models.FloatField(blank=True, null=True)),
                ('deplacement', models.FloatField(blank=True, null=True)),
                ('formation', models.FloatField(blank=True, null=True)),
                ('salaire', models.FloatField(blank=True, null=True)),
                ('cnss', models.FloatField(blank=True, null=True)),
                ('telephone', models.FloatField(blank=True, null=True)),
                ('entretien', models.FloatField(blank=True, null=True)),
                ('ceet', models.FloatField(blank=True, null=True)),
                ('papeterie', models.FloatField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateField(blank=True)),
                ('date_fin', models.DateField(blank=True)),
                ('nc', models.FloatField(blank=True, null=True)),
                ('ac', models.FloatField(blank=True, null=True)),
                ('consulation', models.FloatField(blank=True, null=True)),
                ('vente_pro', models.FloatField(blank=True, null=True)),
                ('actes_soin', models.FloatField(blank=True, null=True)),
                ('analyse', models.FloatField(blank=True, null=True)),
                ('achats_pro', models.FloatField(blank=True, null=True)),
                ('autre_pro', models.FloatField(blank=True, null=True)),
                ('lunette', models.FloatField(blank=True, null=True)),
                ('inam', models.FloatField(blank=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_service', models.CharField(max_length=200, null=True)),
                ('nom_service', models.CharField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_post', models.CharField(max_length=200, null=True)),
                ('nom_post', models.CharField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('type_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='direction.service')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('prenom', models.CharField(max_length=200, null=True)),
                ('date_naissance', models.DateField(blank=True)),
                ('sexe', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('telephone', models.CharField(max_length=200, null=True)),
                ('adresse', models.CharField(max_length=200, null=True)),
                ('nationalite', models.CharField(max_length=200, null=True)),
                ('situation_matrimonial', models.CharField(max_length=200, null=True)),
                ('nombre_enfant', models.IntegerField(blank=True, null=True)),
                ('contrat', models.CharField(max_length=200, null=True)),
                ('date_debut', models.DateField(blank=True)),
                ('date_fin', models.DateField(blank=True)),
                ('personne_prevenir', models.CharField(max_length=200, null=True)),
                ('telephone_prevenir', models.CharField(max_length=200, null=True)),
                ('numero_bank', models.CharField(max_length=200, null=True)),
                ('numero_cnss', models.CharField(max_length=200, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('personne_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='direction.poste')),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('personne_profil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='direction.personnel')),
            ],
        ),
    ]
