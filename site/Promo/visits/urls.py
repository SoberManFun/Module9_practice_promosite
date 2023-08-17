from django.urls import path
from visits.views import visits_p, flats_p, index, houses_p, houses_card_p, companies_p

app_name = 'visits'

urlpatterns = [
    path('', index, name='index'),
    path('visits/', visits_p, name='visits_p'),
    path('flats/', flats_p, name='flats_p'),
    path('houses/', houses_p, name='houses_p'),
    path('houses_card/', houses_card_p, name='houses_card_p'),
    path('companies/', companies_p, name='companies_p'),
]
