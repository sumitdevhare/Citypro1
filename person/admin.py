from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from person.models import Taluka, City, Person,Village

@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display =('city','taluka','village','first_name','middal_name','last_name','phone','addhar','address','image')
    pass
    


admin.site.register(Village)
admin.site.register(Taluka)
admin.site.register(City)
# admin.site.register(Person)