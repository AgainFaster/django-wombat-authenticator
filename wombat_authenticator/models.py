from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

class WombatToken(models.Model):
    class Meta:
        unique_together = (("store", "token"),)

    store = models.CharField(max_length=50)
    token = models.CharField(max_length=50)
    user = models.OneToOneField(AUTH_USER_MODEL, related_name='wombat_auth_token')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s - %s' % (self.store, self.token, self.user)