from django.shortcuts import render
from django.views import View
from site_setting_module.models import settings_site


# Create your views here.
class about_View(View):
    def get(self, request):
        setting = settings_site.objects.filter(Basic_settings=True).first()
        return render(request, 'about_module/about.html', context={
            'setting': setting
        })
