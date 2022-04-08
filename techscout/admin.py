from django.contrib import admin
from .models import SearchTerm, SearchLocation

admin.site.register(SearchTerm)
admin.site.register(SearchLocation)
