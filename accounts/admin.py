from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'gender', 'birthday')
    list_display_links = ('id', 'username', 'email', 'gender', 'birthday')

admin.site.register(User, CustomUserAdmin)