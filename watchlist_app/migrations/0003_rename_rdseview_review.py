# Generated by Django 4.2 on 2023-04-14 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_rdseview'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rdseview',
            new_name='Review',
        ),
    ]
