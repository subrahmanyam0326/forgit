from django.shortcuts import render
from .forms import  RegForm,LogForm
from .models import RegData,LogData
from django.http import HttpResponse
def regview(request):
    if request.method=="POST":
        rform=RegForm(request.POST)
        if rform.is_valid():
            f_name=request.POST.get('f_name')
            l_name=request.POST.get('l_name')
            uname=request.POST.get('uname')
            password=request.POST.get('password')
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
            uname=request.POST.get('uname')
            password=request.POST.get('password')

            user=RegData.objects.filter(uname=uname)
            pwd=RegData.objects.filter(password=password)

            if user and pwd :
                return HttpResponse("success")
            lform=LogForm()
            return render(request,'forgitapp1/log.html',context={'lform':lform})
    lform=LogForm()
    return render(request,'forgitapp1/log.html',context={'lform':lform})




# from django.shortcuts import render
# from .forms import  RegForm,LogForm
# from .models import RegData,LogData
# from django.http import HttpResponse
# def regview(request):
#     if request.method=='POST':
#         rform=RegData(request.POST)
#         if rform.is_
#             f_name = request.POST.get('f_name')
#             l_name = request.POST.get('l_name')
#             uname = request.POST.get('uname')
#
#             password = request.POST.get('password')
#
#
#             data=RegData(
#                 f_name=f_name,
#                 l_name=l_name,
#                 uname=uname,
#                 password=password
#
#             )
#             data.save()
#             lform=LogForm()
#             return render (request,'forgitapp1/log.html',{"abcd":lform})
#
#         else:
#             return HttpResponse("User Missed The Values")
#     else:
#         rform=RegForm()
#         return render (request,'forgitapp1/reg.html',{'hello':rform})
#
#
#
# def login_view(request):
#     if request.method=='POST':
#         lform=LogForm(request.POST)
#         if lform.is_valid():
#             username1=request.POST.get('username')
#             password1=request.POST.get('password')
#             uname=RegistrationData.objects.filter(username=username1)
#             pwd=RegistrationData.objects.filter(password=password1)
#             if uname and pwd:
#                 return HttpResponse("Login Success")
#             else:
#                 rform=RegistrationForm()
#                 return render (request,'regfile.html',{'hello':rform})
#
#         else:
#             return HttpResponse('User Invalid Data')
#     else:
#         lform=LoginForm()
#         return render (request,'logfile.html',{"abcd":lform})