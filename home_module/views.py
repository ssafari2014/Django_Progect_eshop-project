from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from site_setting_module.models import settings_site, Title_of_the_footer_category, Slider
from utils.Convertors import Group_List
from product_module.models import Product, ProductCategory


# Create your views here.


class Home_module_View(TemplateView):
    template_name = 'home_module/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        lists_product = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        most_visit_products: Product = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_Count=Count('productvisit')).order_by('-productvisit')[:12]
        context['lists_product'] = Group_List(lists_product)
        context['most_visit_products'] = Group_List(most_visit_products)
        categories = list(
            ProductCategory.objects.annotate(product_categories_count=Count('product_categories')).filter(is_active=True,
                                                                                                         is_delete=False,
                                                                                                         product_categories_count__gt=0)[
            :6])
        lists_products = []
        for item in categories:
            data = {
                'id': item.id,
                'title': item.title,
                'products': list(item.product_categories.all()[:4])
            }
            lists_products.append(data)

        context['categoris_products'] = lists_products
        return context


class header_partial(TemplateView):
    template_name = 'shired/header_partial.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        setting: settings_site = settings_site.objects.filter(Basic_settings=True).first()
        context['setting'] = setting
        return context


# class footer_partial(TemplateView):
#     template_name = 'shired/footer_partial.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         setting: settings_site = settings_site.objects.filter(Basic_settings=True).first()
#         context['setting'] = setting
#         return context

class footer_partial(View):
    def get(self, request):
        setting: settings_site = settings_site.objects.filter(Basic_settings=True).first()
        footers = Title_of_the_footer_category.objects.all()

        return render(request, 'shired/footer_partial.html', context={
            'setting': setting,
            'footer': footers
        })
