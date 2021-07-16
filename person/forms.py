from django import forms

from person.models import Person, Taluka, City


class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs): #overriding init method to Model form
        super().__init__(*args, **kwargs) # calling parent class or method cunstructor of modelsfrom
        self.fields['taluka'].queryset = Taluka.objects.none() #it takesfilds name of taluka

        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['taluka'].queryset = Taluka.objects.filter(city_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Taluka queryset
        
