from django.contrib import admin
from django.forms import ModelForm, Textarea

from models import Seo



class SeoAdminForm(ModelForm):
    class Meta:
        model = Seo
        widgets = {
            'title': Textarea,
            'keywords': Textarea,
            'description': Textarea,
        }



class SeoAdmin(admin.ModelAdmin):
    form = SeoAdminForm
    list_display = ('loc', 'title', 'changefreq', 'priority', 'lastmod',)
    list_filter = ('changefreq',)
    search_fields = ['loc', 'title', 'keywords', 'description',]
admin.site.register(Seo, SeoAdmin)
