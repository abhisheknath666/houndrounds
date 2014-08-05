from django.db import models

# Create your models here.
class Person(models.Model):
    def __unicode__(self):
        return str(email)
    email = models.EmailField()
    name = models.CharField(max_length=128)

class PetOwner(models.Model):
    def __unicode__(self):
        return str(person)

    person = models.ForeignKey('person')
    pet_access = models.CharField(max_length=128, blank=True, null=True)
    price = models.IntegerField(max_length=128, blank=True, null=True)
    frequency = models.CharField(max_length=128, blank=True, null=True)
    schedule = models.CharField(max_length=128, blank=True, null=True)

class Walker(models.Model):
    def __unicode__(self):
        return str(person)

    person = models.ForeignKey('person')
    price = models.IntegerField(blank=True, null=True)    
