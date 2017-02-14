from django.contrib import admin
from .models import UsersBan,UsersList

class UsersBanModel(admin.ModelAdmin):
    list_display = ['user','ban','permanent']
    list_filter = ('ban','permanent',)
    search_fields = ('user__user','user__first_name','user__last_name')

admin.site.register(UsersBan,UsersBanModel)
