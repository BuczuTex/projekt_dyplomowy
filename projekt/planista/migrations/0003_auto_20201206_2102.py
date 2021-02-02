# Generated by Django 3.1.4 on 2020-12-06 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planista', '0002_auto_20201206_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('elements', models.CharField(max_length=500)),
                ('section', models.CharField(choices=[('ZJ', 'Zjazd'), ('SL', 'Ślub'), ('UR', 'Urodziny'), ('CH', 'Chrzciny')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=6)),
                ('nip', models.IntegerField(max_length=10)),
                ('description', models.CharField(max_length=1000)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=500)),
                ('firm_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planista.firm')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=500)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planista.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='firm_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planista.firm'),
        ),
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
