from django.db import models
from account_module.models import User
from jalali_date import datetime2jalali, date2jalali


# Create your models here.

# category model
class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=400, unique=True, verbose_name='لینک دسته بندی')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقالات'
        verbose_name_plural = 'دسته بندی های مقالات'


# مدل مقالات

class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='لینک مقاله')
    is_active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    img = models.ImageField(upload_to='images/article', verbose_name='تصویر مقاله')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    Relationship_category = models.ManyToManyField(ArticleCategory, verbose_name='ارتباط متن مقاله و دسته بندی')
    auther = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', null=True, editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ')

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


# comment model

class article_comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('article_comments', on_delete=models.CASCADE,
                               verbose_name='دسته بندی کامنت اصلی / پاسخ کامنت',
                               null=True, blank=True)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True,
                                       verbose_name='تاریخ')
    text = models.TextField(verbose_name='متن کامنت')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return str(self.user)
