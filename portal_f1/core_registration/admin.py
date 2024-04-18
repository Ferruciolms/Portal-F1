from django.contrib import admin
from core_registration.models.company import Company
from core_registration.models.country import Country
from core_registration.models.state import State
from core_registration.models.city import City

# Register your models here.
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)