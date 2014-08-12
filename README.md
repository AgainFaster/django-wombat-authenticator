django-wombat-authenticator
===========================
A djangorest authentication module to authenticate incoming requests from Wombat based on the 
X-Hub-Token and X-Hub-Store header fields. Each combination of these headers is considered a
WombatToken model that maps to a Django User model.

To use:

1) Clone this github repository, or install the package by using PIP:
    pip -e git+https://github.com/AgainFaster/django-wombat-authenticator.git#egg=django-wombat-authenticator

2) Add wombat_authenticator to INSTALLED_APPS in the settings.py file of your project.

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

4) Run the wombat_authenticator migration by running the South command:
    ./manage.py migrate wombat_authenticator

5) Create a WombatToken model in the admin. Provide the Store and Token values from Wombat and choose a Django User.

Whenever a request is made to your REST service from Wombat, it will authenticate as the User configured in your
WombatToken model. From here, your application can use the permissions associated with that User.

Always use HTTPS to securely keep the X-Hub-Token and X-Hub-Store headers from Wombat private.
