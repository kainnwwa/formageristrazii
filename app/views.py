from django.shortcuts import render, redirect
from django.contrib.auth import login, logout as auth_logout  
from django.contrib.auth import authenticate
from django.contrib import messages

def glavnay(request):
    return render(request, 'glavnay.html')

def vhod(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('glavnay')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль')
            return render(request, 'vhod.html')
    
    return render(request, 'vhod.html')

def logout_view(request):  
    auth_logout(request)    
    return redirect('glavnay')