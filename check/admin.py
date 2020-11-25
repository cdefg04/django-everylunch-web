from django.contrib import admin
from .models import Check


class CheckAdmin(admin.ModelAdmin):
    list_display = ('time', 'cafeteria', 'menu')


admin.site.register(Check, CheckAdmin)
