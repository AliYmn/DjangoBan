from django.db import models
from django.conf import settings

class UsersBan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name="User name",
                             help_text="Choose Username")

    ban = models.BooleanField(default=False,
                              verbose_name="Ban",
                              help_text="Users Bans")

    class Meta:
        verbose_name_plural = "Ban Management"
        ordering = ('user',)

    def __str__(self):
        return '{}'.format(self.user)
