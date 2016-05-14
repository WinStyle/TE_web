# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('te_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='te_user',
            name='photo',
            field=models.ImageField(default=b'/static/upload_imgs/user-1.jpg', upload_to=b'/static/upload_imgs/'),
            preserve_default=True,
        ),
    ]
