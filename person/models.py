from django.db import models
# from django.utils.timezone import timezone.now

class City(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Taluka(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE) #manay to one realationship 
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Village(models.Model):
    taluka = models.ForeignKey(Taluka, on_delete=models.CASCADE) #manay to one realationship 
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    # name = models.CharField(max_length=12)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    taluka = models.ForeignKey(Taluka, on_delete=models.SET_NULL, blank=True, null=True)
    village = models.ForeignKey(Village, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,null=True)
    middal_name = models.CharField(max_length=50,null=True)
    phone= models.CharField(max_length=15,null=True)
    addhar= models.CharField(max_length=15,null=True)
    address= models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to="person/static/css/img",blank=True, null=True)
    # registration= models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.first_name 
