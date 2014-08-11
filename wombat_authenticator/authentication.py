from rest_framework import authentication
from rest_framework import exceptions

import logging
from wombat_authenticator.models import WombatToken

logger = logging.getLogger(__name__)

class WombatAuthentication(authentication.BaseAuthentication):

    def _log_headers(self, request):

        headers = 'DUMPING HEADERS:\n'

        for key in request.META:
            headers += '\t%s: %s\n' % (key, request.META[key])

        logger.info(headers)

    def authenticate(self, request):
        store = request.META.get('HTTP_X_HUB_STORE')
        token = request.META.get('HTTP_X_HUB_TOKEN')

        if not store or not token:
            logger.info('Authentication credentials were not provided.')
            self._log_headers(request)
            return None

        try:
            token = WombatToken.objects.get(store=store, token=token)
        except WombatToken.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such token.')

        return (token.user, None)