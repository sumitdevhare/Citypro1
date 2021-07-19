
# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
import requests
from .forms import PersonCreationForm
from .models import Person, Taluka,Village
import requests

from import_export import resources
# from .models import Person

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


class PersonResource(resources.ModelResource):
    class Meta:
        model=Person



def person_create_view(request):
    form = PersonCreationForm() # make obj of forms
    print(form)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST) # data argument which send to validatin
        if form.is_valid():
            form.save()
            # success=success(request,"Form Sent successfully")
            return redirect('person_add')
    return render(request, 'persons/home.html', {'form': form})




def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    print(form)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})

# Show Farmer data
def Show_Farmerdata_view(request):
    form1 = PersonCreationForm()
    form = Person.objects.all()
    print(form)
    
    return render(request,'persons/Ftable_data.html',{'form': form,'form1':form1})


# def Get_Talukas(request):
#     city_id = request.GET.get("city_id")
#     talukas = Taluka.objects.filter(city_id=city_id).all()
#     return render(request, 'persons/taluka_dropdown_list_options.html', {'talukas': talukas})
    
# Get village
def Get_Village(request):
    taluka_id = request.GET.get("taluka_id")
    villages = Village.objects.filter(taluka_id=taluka_id).all()
    print(villages)
    return render(request, 'persons/taluka_dropdown_list_options.html', {'villages': villages}) 
    

# Get taluka AJAX
def load_talukas(request):
    city_id = request.GET.get('city_id')
    talukas = Taluka.objects.filter(city_id=city_id).all()
    print(talukas)
    return render(request, 'persons/taluka_dropdown_list_options.html', {'talukas': talukas}) # after render ajax success func run



# fetch Api data into project
def Apiget(request):
    response=requests.get('http://127.0.0.1:8000/person/')
    print(response)
    print("hiii")
    return render(request,'persons/Ftable_data.html',{'response':response})

# GEnerate PDF file 
def venue_pdf(request):
    buf =io.BytesIO()
    # create canvas
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
# test obj
    textob = c.beginText()
    tesxtob.setTextOringin(inch,inch)
    textob.setFont("Helvetica",14)
    
    #Designated Model
    venues = Person.objects.all()
    lines=[]

    #loop
    for  venue in venues:
        lines.append(venue.city)
        lines.append(venue.taluka)
        lines.append(venue.village)
        lines.append(venue.first_name)
        lines.append(venue.middal_name)
        lines.append(venue.last_name)
        lines.append(venue.phone)
        lines.append(venue.addhar)
        lines.append(venue.address)
        lines.append("****************************")


    for line in lines:
        textob.textLine(line)
    #finish Up
        c.drawText(textob)
        c.showPage()
        c.save()
        buf.seek(0)


    #return something
    return FileResponse(buf, as_attachment=True,filename='venue.pdf')

