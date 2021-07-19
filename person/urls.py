from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),# just replace <int:pk> by any ID like 2,4,1 in url serch bar
    path('FD/', views.Show_Farmerdata_view, name='FDperson_add'),
    path('API/', views.Apiget, name='get_api'),
    path('venue_pdf/', views.venue_pdf, name='venue_pdf'),

    path('ajax/load-talukas/', views.load_talukas, name='ajax_load_talukas'),
    path('ajax/load-village/', views.Get_Village, name='ajax_load_village'), # AJAX
]
