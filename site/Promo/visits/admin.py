from django.contrib import admin

from visits.models import House, Flat, FlatContact, Company

admin.site.register(House)
admin.site.register(Flat)
admin.site.register(FlatContact)
admin.site.register(Company)
