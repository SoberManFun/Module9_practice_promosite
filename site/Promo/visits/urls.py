from django.urls import path
from visits.views import visits_p, flats_p, index

app_name = 'visits'

urlpatterns = [
    path('', index, name='index'),
    path('visits/', visits_p, name='visits_p'),
    path('flats/', flats_p, name='flats_p'),
]
