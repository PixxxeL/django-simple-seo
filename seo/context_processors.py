# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.sites.models import Site

from sibno.seo.models import Seo



def seo_page_data(request):
    path = '/' + request.path.strip('/')
    current_site = Site.objects.get_current()
    seo = settings.SEO_DEFAULT_DATA
    try:
        seo = Seo.objects.values(
            'title', 'keywords', 'description'
        ).get(
            loc=path, site=current_site
        )
    except:
        pass
    return { 'seo': seo }
