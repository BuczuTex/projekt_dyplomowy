# Generated by Django 3.1.4 on 2020-12-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planista', '0005_auto_20201206_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='private',
            field=models.BooleanField(default=True),
        ),
    ]
