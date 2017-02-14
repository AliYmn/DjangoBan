from django.db import models

class UsersList(models.Model):
    remote = models.CharField(max_length=100)
    http_x =  models.CharField(max_length=1000)
    http_user = models.CharField(max_length=1000)
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "User List"
        ordering = ('user',)

    def __str__(self):
        return '{}'.format(self.user)

class UsersBan(models.Model):
    user = models.ForeignKey(UsersList,
                             verbose_name="User name",
                             help_text="Choose Username")

    ban = models.BooleanField(default=False,
                              verbose_name="Ban",
                              help_text="Users Bans")

    permanent = models.BooleanField(default=False,
                                    verbose_name="Permanent Ban",
                                    help_text="Banners are unlimited.")

    class Meta:
        verbose_name_plural = "Ban Management"
        ordering = ('user',)

    def __str__(self):
        return '{}'.format(self.user)
