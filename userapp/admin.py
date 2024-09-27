from django.contrib import admin
from .models import Users

# Register your models here.

class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone']
    search_fields = ['=id', 'name', '=phone']

admin.site.register(Users, UsersAdmin)