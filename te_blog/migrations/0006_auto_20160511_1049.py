# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('te_blog', '0005_auto_20160511_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='te_user',
            name='photo',
            field=models.ImageField(default=b'/statics/upload_imgs/back_001.jpg', upload_to=b'/statics/upload_imgs/'),
            preserve_default=True,
        ),
    ]
