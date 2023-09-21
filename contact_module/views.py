from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from .forms import contactUsForms
from . models import ContactUsModel
from site_setting_module.models import settings_site
# Create your views here.

# class Contact_Us_View(FormView):
#     template_name = 'contact_module/app.html'
#     form_class = contactUsForms
#     success_url = '/contact_us/'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class Contact_Us_View(CreateView):
    # model = ContactUsModel
    template_name = 'contact_module/ContactUs.html'
    form_class = contactUsForms
    success_url = '/contact_us/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = settings_site.objects.filter(Basic_settings=True).first()
        context['setting'] = date
        return context

