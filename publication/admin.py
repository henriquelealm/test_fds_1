from django.contrib import admin
from .models import Restaurant
from .models import Review

admin.site.register(Restaurant)
admin.site.register(Review)