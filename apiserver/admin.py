from django.contrib import admin
from .models import User, Channel, User2
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'token']

admin.site.register(User, UserAdmin)

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

class User2Admin(admin.ModelAdmin):
    list_display = ['username', 'token']

admin.site.register(User2, User2Admin)