# Generated by Django 3.2.5 on 2022-04-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wangapp', '0005_auto_20220404_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrast',
            name='state',
            field=models.SmallIntegerField(choices=[(0, '未到期'), (1, '已到期')], default=0, verbose_name='状态'),
        ),
    ]
