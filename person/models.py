from django.db import models


class City(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Taluka(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE) #manay to one realationship 
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    taluka = models.ForeignKey(Taluka, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
