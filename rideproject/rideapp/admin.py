from django.contrib import admin
from .models import Place
from .models import Person

# Register your models here.
admin.site.register(Person)
admin.site.register(Place)
