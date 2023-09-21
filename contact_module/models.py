from django.db import models


# Create your models here.

class ContactUsModel(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان پیام')
    fullname = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    message = models.TextField(max_length=40000, verbose_name='متن پیام')
    date = models.DateField(verbose_name='تاریخ پیام', auto_now_add=True)
    View_Message = models.BooleanField(default=False, verbose_name='پیام دیده شده /پیام دیده نشده', null=True)
    message_admin_answer = models.TextField(max_length=30000, verbose_name='پاسخ ادمین')

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'پیام ها'
        verbose_name_plural = 'تماس با ما'
