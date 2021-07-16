from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),

    path('ajax/load-talukas/', views.load_talukas, name='ajax_load_talukas'), # AJAX
]
