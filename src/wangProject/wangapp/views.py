from django.shortcuts import render,redirect
# from django import forms
# Create your views here.
from wangapp import models
from wangapp.utils.pageination import Pageination
from wangapp.modelform.emp_modelform import EmployeeModelForm,CustomerModelForm,CustomerAddModelForm,\
    ProjectAddModelForm,ProjectModelForm,ContrastAddModelForm,LoginForm


def employee_list(request):
    data_dict={}
    search_value=request.GET.get('q',"")
    if search_value:
        data_dict["job__contains"]=search_value
    queryset=models.FreeEmployee.objects.filter(**data_dict)
    page_object = Pageination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()
    context={
        'queryset':page_queryset,
        'search_value':search_value,
        'page_string':page_string

             }
    return render(request,'employee_list.html',context)



def employee_edit(request,nid):
    row_object=models.FreeEmployee.objects.filter(id=nid).first()
    if request.method=="GET":
        form = EmployeeModelForm(instance=row_object)
        return render(request,'employee_edit.html',{'form':form})
    form=EmployeeModelForm(instance=row_object,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/employee/list/')

    context = {
        'form': form
    }
    return render(request,'employee_edit.html',context)

def employee_delete(request,nid):
    models.FreeEmployee.objects.filter(id=nid).delete()
    return redirect('/employee/list/')

def employee_add(request):
    if request.method=='GET':
        form = EmployeeModelForm()
        return render(request, 'employee_add.html', {'form': form})
    form=EmployeeModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/employee/list/')
    return render(request,'/employee/add/',{'form':form})


def customer_list(request):
    data_dict={}
    search_value=request.GET.get('q',"")
    if search_value:
        data_dict["worktype__contains"]=search_value

    queryset=models.Customer.objects.filter(**data_dict)
    page_object = Pageination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()

    context={
        'queryset':page_queryset,
        'search_value':search_value,
        'page_string':page_string
             }
    return render(request,'customer_list.html',context)

def customer_edit(request,nid):
    row_object=models.Customer.objects.filter(id=nid).first()
    if request.method=="GET":
        form = CustomerModelForm(instance=row_object)
        return render(request,'customer_edit.html',{'form':form})
    form=CustomerModelForm(instance=row_object,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/customer/list/')
    context = {
        'form': form
    }
    return render(request,'customer_edit.html',context)

def customer_delete(request,nid):
    models.Customer.objects.filter(id=nid).delete()
    return redirect('/customer/list/')

def customer_add(request):
    if request.method=='GET':
        form = CustomerAddModelForm()
        return render(request, 'customer_add.html', {'form': form})
    form=CustomerAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/customer/list/')
    return render(request,'customer_add.html',{'form':form})


def project_list(request):
    data_dict={}
    search_value=request.GET.get('q',"")
    if search_value:
        data_dict["projecttype__contains"]=search_value
    queryset=models.ProjectList.objects.filter(**data_dict).order_by('state')
    page_object = Pageination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()
    context={
        'queryset':page_queryset,
        'search_value':search_value,
        'page_string':page_string

             }
    return render(request,'project_list.html',context)

def project_add(request):
    if request.method=='GET':
        form=ProjectAddModelForm()
        return render(request,'project_add.html',{'form':form})
    form=ProjectAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/project/list/')
    return render(request,'project_add.html',{'form':form})

def project_edit(request,nid):
    row_object=models.ProjectList.objects.filter(id=nid).first()
    if request.method=="GET":
        form = ProjectModelForm(instance=row_object)
        return render(request,'project_edit.html',{'form':form})
    form=ProjectModelForm(instance=row_object,data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/project/list/')
    context = {
        'form': form
    }
    return render(request,'project_edit.html',context)

def contrast_list(request):
    data_dict={}
    search_value=request.GET.get('q',"")
    if search_value:
        data_dict["worker__contains"]=search_value
    queryset=models.Contrast.objects.filter(**data_dict)
    page_object = Pageination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()
    context={
        'queryset':page_queryset,
        'search_value':search_value,
        'page_string':page_string

             }
    return render(request,'contrast_list.html',context)

def contrast_add(request):
    if request.method=='GET':

        form=ContrastAddModelForm()
        return render(request,'contrast_add.html',{'form':form})

    form=ContrastAddModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/contrast/list/')
    return render(request,'contrast_add.html',{'form':form})

def contrast_delete(request,nid):
    models.Contrast.objects.filter(id=nid).delete()
    return redirect('/contrast/list/')


def login_page(request):
    if request.method=='GET':
        form=LoginForm()
        return render(request, 'login_page.html',{'form':form})
    form=LoginForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        emp_object=models.FreeEmployee.objects.filter(**form.cleaned_data).first()
        admin_object=models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            if not emp_object:
                form.add_error('password','用户名或密码错误')
                return render(request, 'login_page.html', {'form': form})
            request.session['info'] = {'id': emp_object.id, 'name': emp_object.name}
            return redirect('/emp/selflist/')
        request.session['info'] = {'id': admin_object.id, 'user_name': admin_object.name}
        return redirect('/employee/list/')
    return render(request,'login_page.html',{'form':form})

def logout(request):
    request.session.clear()
    return redirect('/login/')


def emp_selflist(request):
    queryset=models.Contrast.objects.filter(worker__name=request.session.get("info")['name'])
    return render(request,'emp_selflist.html',{'queryset':queryset})







