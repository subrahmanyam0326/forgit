from django.shortcuts import render
from .forms import  RegForm,LogForm
from .models import RegData,LogData
from django.http import HttpResponse
def regview(request):
    if request.method=="POST":
        rform=RegForm(request.POST)
        if rform.is_valid():
            f_name=request.post.get('f_name')
            l_name=request.post.get('l_name')
            uname=request.post.get('uname')
            password=request.post.get('password')
            data=RegData(
                f_name=f_name,
                l_name=l_name,
                uname=uname,
                password=password
            )
            data.save()
            lform=LogForm()
            return render(request,'forgitapp1/reg.html',{'lfom':lform})
    rform=RegForm()
    context={'rform':rform}
    return render (request,'forgitapp1/reg.html',context)
def logview(request):
    if request.method=="POST":
        lform=LogForm(request.POST)
        if lform.is_valid():
            uname=request.post.get('uname')
            password=request.post.get('password')

            user=RegData.objects.filter(uname=uname)
            pwd=RegData.objects.filter(password=password)

            if user and pwd :
                return HttpResponse("success")
            lform=LogForm()
            return render(request,'forgitapp1/log.html',context={'lform':lform})
    lform=LogForm()
    return render(request,'forgitapp1/log.html',context={'lform':lform})




