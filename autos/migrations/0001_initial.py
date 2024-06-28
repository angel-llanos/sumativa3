# Generated by Django 4.1.2 on 2024-06-27 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id_autos', models.AutoField(db_column='id_autos', primary_key=True, serialize=False)),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField(max_length=4)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]