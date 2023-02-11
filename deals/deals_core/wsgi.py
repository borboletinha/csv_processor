import os
from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deals.deals_core.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root='deals/deals/static')
