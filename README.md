django-wombat-authenticator
===========================
A djangorest authentication module to authenticate incoming requests from Wombat based on the 
HUB_STORE and HUB_TOKEN header fields. Each combination of these headers is considered a
WombatToken model that maps to a user.

To use:

1) Create a WombatToken model in the admin. Provide the Store and Token values from Wombat and set a Django User.

2) Add wombat_authenticator to INSTALLED_APPS in settings.py.

3) In settings.py add 'wombat_authenticator.authentication.WombatAuthentication' to DEFAULT_AUTHENTICATION_CLASSES
list within the REST_FRAMEWORK dictionary. 

For example:

REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'wombat_authenticator.authentication.WombatAuthentication',
    )
}
        
Whenever a request is made to your REST service from Wombat, it will authenticate as the User configured in your
WombatToken model. From here, your application can use the permissions associated with that user. 

Always use HTTPS to securely keep the HUB_STORE and HUB_TOKEN headers from Wombat private.
