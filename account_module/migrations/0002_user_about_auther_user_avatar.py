# Generated by Django 4.2.3 on 2023-08-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_auther',
            field=models.TextField(blank=True, null=True, verbose_name='متن نویسنده'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/article_user', verbose_name='تصویر کامنت نویسنده'),
        ),
    ]