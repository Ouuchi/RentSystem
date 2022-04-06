from django.db import models

# Create your models here.
class Admin(models.Model):
    name=models.CharField(verbose_name="姓名",max_length=32)
    password=models.CharField(verbose_name="密码",max_length=32,default=None)


class FreeEmployee(models.Model):
    name=models.CharField(verbose_name="姓名",max_length=32)
    password=models.CharField(verbose_name="密码",max_length=32,default=None)
    job=models.CharField(verbose_name="工作类型",max_length=32)
    email=models.CharField(verbose_name="邮箱",max_length=32)
    phone_number=models.CharField(verbose_name="手机号码",max_length=11)



    def __str__(self):
        return self.name


class Customer(models.Model):
    companyname=models.CharField(verbose_name="公司名称",max_length=32)
    worktype=models.CharField(verbose_name="行业",max_length=32)
    def __str__(self):
        return self.companyname
# 项目表
class ProjectList(models.Model):
    projectname=models.CharField(verbose_name="项目名",max_length=32)
    state_choice = (
        (0, "闲置"),
        (1, "进行中"),
    )
    projecttype=models.CharField(verbose_name="项目类型",max_length=32,default=None)
    state=models.SmallIntegerField(verbose_name="状态",choices=state_choice,default=0)
    responser=models.ForeignKey(verbose_name="负责人",to="FreeEmployee",to_field="id",null=True,blank=True,on_delete=models.SET_NULL,default=None)

#合同表
class Contrast(models.Model):
    name = models.CharField(verbose_name="合同名", max_length=32, default=None)
    companyname=models.ForeignKey(verbose_name="公司名(客户)",to='Customer',to_field='id',null=True,blank=True,on_delete=models.SET_NULL,default=None)
    # 自由职业者工人去合同中公司工作
    worker=models.ForeignKey(verbose_name="自由职业者姓名",to='FreeEmployee',to_field='id',null=True,blank=True,on_delete=models.SET_NULL,default=None)
    start=models.DateField(verbose_name="签订时间")
    end=models.DateField(verbose_name="合同到期时间")
    state_choice = (
        (0, "未到期"),
        (1, "进行中"),
        (2, "已到期"),
    )
    state=models.SmallIntegerField(verbose_name="状态",choices=state_choice,default=0)




