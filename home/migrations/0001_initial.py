# Generated by Django 4.1 on 2022-10-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home_notizia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_notizia', models.TextField()),
                ('descrizione', models.TextField()),
                ('immagine', models.ImageField(upload_to='')),
            ],
        ),
    ]