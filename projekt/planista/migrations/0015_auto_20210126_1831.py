# Generated by Django 3.1.4 on 2021-01-26 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planista', '0014_auto_20210126_1829'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opinion',
            old_name='firm',
            new_name='company',
        ),
    ]
