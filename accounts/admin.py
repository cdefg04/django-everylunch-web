from django.contrib import admin
from .models import myuser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'school', 'cafeteria')


admin.site.register(myuser, MyUserAdmin)