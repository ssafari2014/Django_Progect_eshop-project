# Generated by Django 4.2.3 on 2023-08-28 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0008_alter_article_comments_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article_comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.article_comments', verbose_name='دسته بندی کامنت اصلی / پاسخ کامنت'),
        ),
    ]