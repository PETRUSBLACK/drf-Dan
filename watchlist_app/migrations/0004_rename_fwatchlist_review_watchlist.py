# Generated by Django 4.2 on 2023-04-14 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0003_rename_rdseview_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='fwatchlist',
            new_name='watchlist',
        ),
    ]
