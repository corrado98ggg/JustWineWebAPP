# Generated by Django 4.1 on 2022-10-18 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contattaci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_contattare', models.TextField()),
                ('cognome_da_contattare', models.TextField()),
                ('paese', models.TextField()),
                ('email', models.TextField()),
                ('oggetto', models.TextField()),
            ],
        ),
    ]