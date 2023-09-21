from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email_active_code = models.CharField(max_length=300, verbose_name='کد فعالسازی ایمیل')
    avatar = models.ImageField(upload_to='images/article_user', verbose_name='تصویر کامنت نویسنده', null=True, blank=True)
    about_auther = models.TextField(verbose_name='متن نویسنده', blank=True, null=True)
    address = models.TextField(null=True, blank=True, verbose_name='ادرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران سایت'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
