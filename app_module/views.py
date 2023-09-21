from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from .forms import app_Form
from .models import apps_Upload_File
from django.views.generic.edit import CreateView


# Create your views here.

def my_filed(file):
    with open('temp/image', 'wb+') as files:
        for chunk in file.chunks():
            files.write(chunk)


class APP_View(CreateView):
    template_name = 'app_module/app.html'
    model = apps_Upload_File
    fields = '__all__'
    success_url = '/app_module'


# class APP_View(View):
#     def get(self, request):
#         appForm = app_Form()
#         return render(request, 'app_module/app.html', context={
#             'form': appForm
#         })
#
#     def post(self, request):
#         appForm2 = app_Form(request.POST, request.FILES)
#         if appForm2.is_valid():
#             apps_upload_file = apps_Upload_File(file=request.FILES['my_form'])
#             apps_upload_file.save()
#             return redirect('/contact_us/')
#         else:
#             return render(request, 'app_module/app.html', context={
#                 'form': appForm2
#             })

class ProfileView(ListView):
    model = apps_Upload_File
    template_name = 'app_module/profileView.html'
    context_object_name = 'profiles'
