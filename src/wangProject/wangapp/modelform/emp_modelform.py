from django import forms
from wangapp import models

from django.core.exceptions import ValidationError
class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = models.FreeEmployee
        fields = ['name','password','job', 'email', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['companyname','worktype']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control'}

class CustomerAddModelForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['companyname','worktype']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}

    def clean_companyname(self):
        txt_companyname=self.cleaned_data["companyname"]
        name_exists=models.Customer.objects.filter(companyname=txt_companyname).exists()
        if name_exists :
            raise ValidationError("该客户已存在")
        return txt_companyname


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model=models.ProjectList
        fields=['projectname','projecttype','state','responser']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}



class ProjectAddModelForm(forms.ModelForm):
    class Meta:
        model=models.ProjectList
        fields=['projectname','projecttype','state','responser']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}

    def clean_projectname(self):
        txt_projectname=self.cleaned_data["projectname"]
        exists=models.ProjectList.objects.filter(projectname=txt_projectname).exists()
        if exists:
            raise ValidationError("项目已存在")
        return txt_projectname

class ContrastAddModelForm(forms.ModelForm):
    class Meta:
        model=models.Contrast

        fields=['name','companyname','worker','start','end','state']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs={'class':'form-control'}


    def clean_name(self):
        txt_name=self.cleaned_data["name"]
        exists=models.Contrast.objects.filter(name=txt_name).exists()
        if exists:
            raise ValidationError("合同已存在")
        return txt_name

    def clean_start(self):
        txt_start=self.cleaned_data["start"]
        print(type(txt_start),txt_start)
        print(models.Contrast.objects.all().count())
        if models.Contrast.objects.filter(worker=self.cleaned_data["worker"]).count()==0:
            return txt_start
        worker_lastendtime = models.Contrast.objects.filter(worker=self.cleaned_data["worker"]).values("end").order_by("end").last()["end"]
        if txt_start<worker_lastendtime:
            raise ValidationError("该自由职业者在{}之前都有工作安排".format(worker_lastendtime))
        return txt_start



class LoginForm(forms.Form):
    name=forms.CharField(label="用户名",widget=forms.TextInput,required=True)
    password=forms.CharField(label="密码",widget=forms.PasswordInput,required=True)
    name.widget.attrs = {'class': 'form-control'}
    password.widget.attrs = {'class': 'form-control'}






