# Generated by Django 4.0.3 on 2022-06-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingUpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=30)),
                ('Brith_Date', models.DateField(null=True)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
