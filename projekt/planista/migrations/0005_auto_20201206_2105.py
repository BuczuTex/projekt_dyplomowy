# Generated by Django 3.1.4 on 2020-12-06 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planista', '0004_auto_20201206_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='firm_id',
            new_name='firm',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='firm',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='firm_id',
            new_name='firm',
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='user_id',
            new_name='user',
        ),
    ]
