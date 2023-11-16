from django.urls import path
from visits.views import visits, flats, index, houses, houses_card, companies, add_visit, edit_visit, houses_edit, \
    flats_edit, flat_contact_add, usercompanyadd, statistics_door, statistics_reaction


app_name = 'visits'

urlpatterns = [
    path('', index, name='index'),
    path('visits/', visits, name='visits_p'),
    path('visits/add_visit/', add_visit, name='add_visit_p'),
    path('visits/edit_visit/<int:visit_id>/', edit_visit, name='edit_visit_p'),
    path('flats/', flats, name='flats_p'),
    path('flats/edit_flat/<int:flat_id>/', flats_edit, name='flats_edit_p'),
    path('flats/flat_contact/edit/<int:flat_id>/', flat_contact_add, name='flat_contact_add'),
    path('houses/', houses, name='houses_p'),
    path('visits/edit_house/<int:house_id>/', houses_edit, name='edit_house_p'),
    path('houses_card/', houses_card, name='houses_card_p'),
    path('companies/', companies, name='companies_p'),
    path('company/add/<int:company_id>/', usercompanyadd, name='usercompanyadd'),
    path('visits/statistics_door/', statistics_door, name='statistics_door'),
    path('visits/statistics_reaction/', statistics_reaction, name='statistics_reaction'),
]
