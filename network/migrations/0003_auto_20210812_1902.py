# Generated by Django 3.2.6 on 2021-08-12 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('network', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Post creation date'),
        ),
        migrations.AddField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.customuser', verbose_name='Post author'),
            preserve_default=False,
        ),
    ]
