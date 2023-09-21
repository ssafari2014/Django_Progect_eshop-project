from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
from jalali_date import datetime2jalali, date2jalali
from .models import ArticleCategory, article_comments


# Create your views here.


class Article_List_View(ListView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_module/article_list.html'
    paginate_by = 1

    def get_context_data(self, *args, **kwargs):
        context = super(Article_List_View, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(Article_List_View, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')  # url
        if category_name is not None:
            query = query.filter(Relationship_category__url_title__iexact=category_name)
        return query


def article_category_partial(request: HttpRequest):
    article_main_category = ArticleCategory.objects.prefetch_related('articlecategory_set').filter(is_active=True,
                                                                                                   parent=None)
    return render(request, 'article_module/include/article_category_partial.html', context={
        'article_main_category': article_main_category
    })


class Article_Detail(DetailView):
    model = Article
    # context_object_name = 'article-detail'
    template_name = 'article_module/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super(Article_Detail, self).get_context_data(**kwargs)
        Article_a: Article = kwargs.get('object')
        context['comment'] = article_comments.objects.filter(article_id=Article_a.id, parent=None).order_by('-create_date').prefetch_related(
            'article_comments_set')
        return context

        # context['comment'] = kwargs
        # print(kwargs)

        # article: Article = kwargs('object')
        # context = article_comments.objects.filter(article_id=article)
        # return context


def add_article_comment(request: HttpRequest):
    # print(request.GET)
    if request.user.is_authenticated:
        article_id = request.GET.get('article_id')
        article_comment = request.GET.get('article_comment')
        parent_id = request.GET.get('parent_id')
        new_comment = article_comments(
            article_id=article_id,
            text=article_comment,
            user_id=request.user.id,
            parent_id=parent_id,
        )
        new_comment.save()

    return HttpResponse('hello')
