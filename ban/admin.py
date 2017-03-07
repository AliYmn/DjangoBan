from django.contrib import admin
from .models import UsersBan

class UsersBanModel(admin.ModelAdmin):
    list_display = ['user','ban',]
    list_filter = ('ban',)
    search_fields = ('user__username','user__id','user__first_name','user__last_name')

admin.site.register(UsersBan,UsersBanModel)
