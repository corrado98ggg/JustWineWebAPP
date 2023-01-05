# Generated by Django 4.1 on 2022-10-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Malattia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_malattia', models.TextField()),
                ('descrizione', models.TextField()),
                ('sintomi_riassunti', models.TextField()),
                ('difesa', models.TextField()),
                ('immagine', models.ImageField(upload_to='')),
            ],
        ),
    ]
