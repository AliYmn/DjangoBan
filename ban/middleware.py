from .models import UsersBan
from django.conf import settings
from django.shortcuts import render


class BanManagement():
    """Users Management"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if(UsersBan.objects.all().filter(ban=True,user_id=request.user.id)):
            return render(request,'ban.html',locals())
        else:
            return response