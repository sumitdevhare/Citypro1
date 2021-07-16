from django.contrib import admin

# Register your models here.
from person.models import Taluka, City, Person

admin.site.register(Taluka)
admin.site.register(City)
admin.site.register(Person)