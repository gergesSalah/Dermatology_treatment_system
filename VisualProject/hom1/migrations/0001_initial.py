# Generated by Django 4.0.3 on 2022-06-24 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home_Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_Advert', models.CharField(max_length=4)),
                ('prodect', models.CharField(max_length=40)),
                ('describes', models.TextField(max_length=300)),
                ('img', models.ImageField(blank=True, null=True, upload_to='filepath')),
                ('link', models.CharField(max_length=300)),
            ],
        ),
    ]