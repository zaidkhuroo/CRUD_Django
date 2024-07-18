from django.contrib import admin

# Register your models here.
from .models import Entries

admin.site.register(Entries)