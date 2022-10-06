from django.contrib import admin
from .models import Feather, Finch, Sighting
# Register your models here.
admin.site.register(Finch)
admin.site.register(Sighting)
admin.site.register(Feather)