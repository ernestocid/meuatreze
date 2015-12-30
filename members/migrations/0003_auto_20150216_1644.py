# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_is_department_leader'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='member',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
