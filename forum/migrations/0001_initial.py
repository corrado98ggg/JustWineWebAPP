# Generated by Django 4.1.3 on 2022-12-07 11:47

from django.db import migrations, models
import django.db.models.deletion
import forum.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default='anonimo', max_length=30)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('topic', models.CharField(max_length=230)),
                ('descrizione', models.TextField(blank=True)),
                ('slug_title', models.SlugField(default=forum.models.randomString)),
            ],
        ),
        migrations.CreateModel(
            name='Partecipa_vero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partecipa', models.BooleanField()),
                ('user_che_partecipa', models.CharField(default='anonimo', max_length=50)),
                ('nome_topic_forum', models.ForeignKey(blank=True, default='ciao', on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
            ],
        ),
        migrations.CreateModel(
            name='Discussione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_forum_associato', models.CharField(default='anonimo', max_length=30)),
                ('discuss', models.TextField()),
                ('username', models.CharField(default='anonimo', max_length=30)),
                ('forum', models.ForeignKey(blank=True, default='anonimo', on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
            ],
        ),
    ]
