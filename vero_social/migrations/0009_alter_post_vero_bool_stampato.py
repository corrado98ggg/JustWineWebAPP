# Generated by Django 4.1.3 on 2022-12-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vero_social', '0008_alter_post_vero_bool_stampato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_vero',
            name='bool_stampato',
            field=models.BooleanField(default=False),
        ),
    ]
