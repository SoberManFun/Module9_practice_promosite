from django.urls import path
from visits.views import visits, flats, index, houses, houses_card, companies, add_visit

app_name = 'visits'

urlpatterns = [
    path('', index, name='index'),
    path('visits/', visits, name='visits_p'),
    path('visits/add_visit/', add_visit, name='add_visit_p'),
    path('flats/', flats, name='flats_p'),
    path('houses/', houses, name='houses_p'),
    path('houses_card/', houses_card, name='houses_card_p'),
    path('companies/', companies, name='companies_p'),
]
