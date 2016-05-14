# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('te_blog', '0002_auto_20160511_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='te_user',
            name='photo',
            field=models.ImageField(default=b'upload_imgs/user-1.jpg', upload_to=b'upload_imgs/'),
            preserve_default=True,
        ),
    ]
