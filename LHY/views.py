from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    u=request.POST.get("user",'')
    p=request.POST.get("pwd",'')
    if u and p:
        c = StudentInfo.objects.filter(stu_name=u, stu_psw=p).exists()
        if c:
            return HttpResponse("success!")
        else:
            return render(request,"back_login.html", {"data":"err user or err password"})
    else:
        return render(request,"back_login.html", {"data": "enter right user and password"})



def toRegister_view(request):
    return render(request,'register.html')

i=5
def Register_view(request):
    u = request.POST.get("user",'')
    p = request.POST.get("pwd",'')
    global i
    i=i+1
    if u and p:
        c = StudentInfo.objects.filter(stu_name=u).exists()
        if c:
            return HttpResponse("user already exists")
        stu = StudentInfo(stu_id=i, stu_name=u, stu_psw=p)
        stu.save()
        return render(request,"back_register.html", {"data":"register success\n,stu_id:{id}  stu_name:{name}  stu_psw:{psw}".format(id=i,name = u,psw=p)})

    else:
        return render(request,"back_register.html", {"data":"enter right user and password"})

