from django.contrib import admin
from wombat_authenticator.models import WombatToken


class WombatTokenAdmin(admin.ModelAdmin):
    pass

admin.site.register(WombatToken, WombatTokenAdmin)