"""
WSGI config for tst_tc3642_qgsxmcpr_72716 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tst_tc3642_qgsxmcpr_72716.settings')

application = get_wsgi_application()
