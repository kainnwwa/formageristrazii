from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def glavnay(request):
    return render(request, 'glavnay.html')

@login_required
def lichni(request):
    context = {
        'username': request.user.username
    }
    return render(request, 'lichni.html', context)
