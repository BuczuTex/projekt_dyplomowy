# Generated by Django 3.1.4 on 2021-01-26 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planista', '0013_auto_20210126_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='event_id',
            new_name='event',
        ),
    ]
