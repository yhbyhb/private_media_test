# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import private_media.storages


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publicFile', models.FileField(upload_to=b'')),
                ('privateFile', models.FileField(storage=private_media.storages.PrivateMediaStorage(), upload_to=b'')),
            ],
        ),
    ]
