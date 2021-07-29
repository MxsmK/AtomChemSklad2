from django.contrib import admin
from .models import React


class ReactAdmin(admin.ModelAdmin):
    list_display = ('name', 'qual', 'clas', 'date', 'prov', 'srok', 'place', 'mass')
    list_filter = ('srok', 'name')
    search_fields = ('name', 'qual', 'prov')
    date_hierarchy = 'srok'


admin.site.register(React, ReactAdmin)
