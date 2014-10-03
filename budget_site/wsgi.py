"""
WSGI config for budget_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import locale

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "budget_site.settings")

#from budget_site.settings import
locale.setlocale(locale.LC_ALL, '')  # TO DO: set the locale on a user basis?

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
