# Generated by Django 2.2.3 on 2019-07-03 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
        ('hero', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hero',
            unique_together={('name', 'movie')},
        ),
    ]
