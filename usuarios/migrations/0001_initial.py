# Generated by Django 4.1.2 on 2024-06-30 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('contrasena', models.CharField(max_length=50)),
            ],
        ),
    ]
