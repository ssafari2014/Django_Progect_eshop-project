# Generated by Django 4.2.3 on 2023-08-23 17:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article_module', '0005_alter_article_auther'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2023, 8, 23), verbose_name='تاریخ'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='auther',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نویسنده'),
        ),
    ]