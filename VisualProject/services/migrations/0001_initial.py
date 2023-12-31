# Generated by Django 4.0.5 on 2022-06-26 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=25, null=True)),
                ('name', models.CharField(max_length=50)),
                ('reg_date', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=25, null=True)),
                ('name', models.CharField(max_length=50)),
                ('reg_date', models.DateTimeField(auto_now=True, null=True)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='patientdiseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='images/')),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='treatments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Indications', models.CharField(max_length=500)),
                ('Contraindications', models.CharField(max_length=500, null=True)),
                ('price', models.FloatField()),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treat_dises', to='services.diseases')),
            ],
        ),
        migrations.CreateModel(
            name='pharmacies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('rate', models.FloatField()),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='area_pharc', to='services.areas')),
            ],
        ),
    ]
