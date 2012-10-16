# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.sites.models import Site



URL_FREQUENCY = (
    ('always',  u'Постоянно',),
    ('hourly',  u'Каждый час',),
    ('daily',   u'Ежедневно',),
    ('weekly',  u'Еженедельно',),
    ('monthly', u'Ежемесячно',),
    ('yearly',  u'Ежегодно',),
    ('never',   u'Никогда',),
)
class Seo(models.Model):
    '''
    SEO - данные
    '''
    loc = models.CharField(
        verbose_name = u'URL без домена',
        help_text = u'Например: /contacts',
        max_length = 2048,
        #unique = True,
    )
    title = models.CharField(
        verbose_name = u'Название',
        max_length = 255,
    )
    keywords = models.CharField(
        verbose_name = u'Ключевые слова',
        max_length = 255,
        blank = True, null = True,
    )
    description = models.CharField(
        verbose_name = u'Описание',
        max_length = 512,
        blank = True, null = True,
    )
    changefreq = models.CharField(
        verbose_name = u'Частота изменения',
        max_length = 8,
        choices = URL_FREQUENCY,
        default = URL_FREQUENCY[4][0],
    )
    priority = models.FloatField(
        verbose_name = u'Приоритетность',
        help_text = u'От 0 до 1',
        default = .5,
    )
    lastmod = models.DateTimeField(
        verbose_name = u'Дата последнего изменения',
        blank = True, null = True,
    )
    site = models.ForeignKey(
        Site,
        verbose_name = u'Сайт',
    )


    __unicode__ = lambda self: self.loc
    
    
    def save(self, *args, **kwargs):
        if self.priority > 1: self.priority = 1
        elif self.priority < 0: self.priority = 0
        if self.loc != '/':
            self.loc = '/' + self.loc.strip('/')
        super(Seo, self).save(*args, **kwargs)


    class Meta:
        verbose_name = u'SEO-данные'
        verbose_name_plural = u'SEO-данные'
