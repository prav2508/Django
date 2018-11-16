from django.db import models

class Pet(models.Model):
    SEX_OPTIONS = [('m','male'),('f','female')]
    name = models.CharField(max_length=200)
    submitter = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_OPTIONS,max_length=1)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
