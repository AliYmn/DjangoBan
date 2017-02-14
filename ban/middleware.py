from .models import UsersList,UsersBan
from django.http import HttpResponse
from django.conf import settings


ban_message = getattr(settings, "BAN_MESSAGE", "You were banned by administrator.")
permanent_ban_message = getattr(settings, "PERMANENT_BAN_MESSAGE", "You were unlimited ban by administrator.")
BAN_DESCRIPTION = getattr(settings, "BAN_DESCRIPTION", "Reason: Rule violation.")

message = """
<html>
<head>
<br><br><br><br>
<center><h1>{}<h1></center>
</head>

<body>
<center>
<mark><b>{}</b></mark>
</center>
</body>

</html>
"""

class BanManagement():
    """Users Management"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)



        if(UsersBan.objects.all().filter(ban=True,user__user=str(request.user),
                                         permanent=True,
                                         user__remote=str(request.META.get('REMOTE_ADDR')),
                                         user__http_x=str(request.META.get('HTTP_X_FORWARDED_FOR')),
                                         user__http_user=str(request.META['HTTP_USER_AGENT']))):

            return HttpResponse(message.format(permanent_ban_message,BAN_DESCRIPTION))

        else:

            if(UsersBan.objects.all().filter(ban=True,
                                             permanent=True,
                                             user__remote=str(request.META.get('REMOTE_ADDR')),
                                             user__http_x=str(request.META.get('HTTP_X_FORWARDED_FOR')),
                                             user__http_user=str(request.META['HTTP_USER_AGENT']))):

                return HttpResponse(message.format(permanent_ban_message, BAN_DESCRIPTION))

            else:

                if(UsersBan.objects.all().filter(ban=True,user__user=str(request.user))):
                    return HttpResponse(message.format(ban_message, BAN_DESCRIPTION))

                else:

                    if(UsersList.objects.all().filter(user=str(request.user))):
                        return response

                    else:

                        if(request.user.is_active):
                            UsersList.objects.create(remote=str(request.META.get('REMOTE_ADDR')),
                                                http_x=str(request.META.get('HTTP_X_FORWARDED_FOR')),
                                                http_user=str(request.META['HTTP_USER_AGENT']),
                                                user=str(request.user),
                                                name=str(request.user.first_name),
                                                surname=str(request.user.last_name)).save()

        return response