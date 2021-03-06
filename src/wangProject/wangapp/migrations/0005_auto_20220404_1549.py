# Generated by Django 3.2.5 on 2022-04-04 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wangapp', '0004_projectlist_projecttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlist',
            name='projecttype',
            field=models.CharField(default=None, max_length=32, verbose_name='项目类型'),
        ),
        migrations.CreateModel(
            name='Contrast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='签订时间')),
                ('end', models.DateField(verbose_name='合同到期时间')),
                ('companyname', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wangapp.customer', verbose_name='公司名(客户)')),
                ('worker', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wangapp.freeemployee', verbose_name='自由职业者姓名')),
            ],
        ),
    ]
