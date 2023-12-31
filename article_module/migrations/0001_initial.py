# Generated by Django 4.2.3 on 2023-08-21 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان دسته بندی')),
                ('url_title', models.CharField(max_length=400, unique=True, verbose_name='لینک دسته بندی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecategory')),
            ],
            options={
                'verbose_name': 'دسته بندی مقالات',
                'verbose_name_plural': 'دسته بندی های مقالات',
            },
        ),
    ]
