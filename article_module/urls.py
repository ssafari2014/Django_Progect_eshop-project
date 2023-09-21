from django.urls import path
from . import views

urlpatterns = [
    path('', views.Article_List_View.as_view(), name='article-list'),
    path('cat/<str:category>', views.Article_List_View.as_view(), name='article-category-list'),
    path('add-article-comment', views.add_article_comment, name='add-article-comment'),
    path('<pk>', views.Article_Detail.as_view(), name='article-category-detail'),

]
