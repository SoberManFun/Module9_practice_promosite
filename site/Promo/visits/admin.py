from django.contrib import admin

from visits.models import House, Flat, FlatContact

admin.site.register(House)
admin.site.register(Flat)
admin.site.register(FlatContact)
