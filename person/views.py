
# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .forms import PersonCreationForm
from .models import Person, Taluka


def person_create_view(request):
    form = PersonCreationForm() # make obj of forms
    if request.method == 'POST':
        form = PersonCreationForm(request.POST) # data argument which send to validatin
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'persons/home.html', {'form': form})





# AJAX
def load_talukas(request):
    city_id = request.GET.get('city_id')
    talukas = Taluka.objects.filter(city_id=city_id).all()
    return render(request, 'persons/taluka_dropdown_list_options.html', {'talukas': talukas}) # after render ajax success func run
    
