# Generated by Django 2.2.7 on 2019-11-16 15:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_content', models.TextField()),
                ('post_date', models.DateTimeField(default=datetime.datetime.now)),
                ('post_photo', models.ImageField(blank=True, upload_to='photos/%/%m/%d/')),
                ('post_likes', models.IntegerField(default=0)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]