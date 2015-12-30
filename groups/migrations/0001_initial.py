# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('leader', models.ForeignKey(to='members.Member')),
                ('members', models.ManyToManyField(related_name='member_groups', to='members.Member', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('comments', models.TextField()),
                ('type', models.CharField(default=b'ST', max_length=2, choices=[(b'ST', b'Estudo'), (b'RE', b'Relacionamento')])),
                ('group', models.ForeignKey(to='groups.Group')),
                ('members_who_attended', models.ManyToManyField(to='members.Member', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
