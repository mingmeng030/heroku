from django.shortcuts import render
from django.shortcuts import redirect
#User에 대한 클래스 가져오기
from django.contrib.auth.models import User
#계정에 관한 권한 가져오기
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            #user가 none 이 아닐 때==user가 존재할 때
            auth.login(request, user)
            return redirect('home')
        else:
            #user가 없을 때->로그인 거부
            return render(request, 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        redirect('home')
    return render(request,'login.html')