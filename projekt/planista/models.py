from django.core.files.storage import FileSystemStorage
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

fs = FileSystemStorage(location='/media/images')

class User(AbstractUser):
    avatar = models.ImageField(storage = fs, default = "media/images/default.png")
    role = models.CharField(max_length = 13)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 50)


class Company(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 6)
    nip = models.IntegerField(validators=[MaxValueValidator(999999999)])
    description = models.CharField(max_length = 1000)
    views = models.IntegerField(default=0)


class Opinion(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    contents = models.CharField(max_length = 500)
    add_date = models.DateTimeField(default = None)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    elements = models.CharField(max_length = 500)
    section_choices = (
        ("ZJ", "Zjazd"),
        ("SL", "Ślub"),
        ("UR", "Urodziny"),
        ("CH", "Chrzciny"),
    )
    section = models.CharField(choices=section_choices, max_length = 2)


class Note(models.Model):
    event = models.ForeignKey(Event, on_delete = models.CASCADE)
    contents = models.CharField(max_length = 500)
    modification_date = models.DateTimeField