# Generated by Django 3.1.4 on 2020-12-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planista', '0008_auto_20201207_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='media/images/default.png', upload_to='media/images/'),
        ),
    ]
