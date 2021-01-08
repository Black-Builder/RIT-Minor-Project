from django.db import models

# Create your models here.
class signupform(models.Model):
    firstname = models.CharField( max_length=50)
    lastname = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    mobile = models.IntegerField
    email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)

class loginform(models.Model):
    name = models.CharField( max_length=50)
    password = models.CharField( max_length=50)

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.TextField(max_length=500)

class Feedback(models.Model):
    option1 = models.CharField(max_length=500)
    option2 = models.CharField(max_length=500)
    option3 = models.CharField(max_length=500)
    identity = models.EmailField()

class Timetable(models.Model):
    name = models.CharField(max_length=20)
    timetable = models.FileField()

class Newsupdate(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    files = models.FileField()

class Importantlink(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)    