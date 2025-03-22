from django.shortcuts import render
from .utils import send_email
# Create your views here.
def welcome(request):
    context = {
        'title': 'It\'s me',
    }
    return render(request, 'main/welcome.html', context)

def welcome_ru(request):
    context = {
        'title': 'Это я',
    }
    return render(request, 'main/welcome-ru.html', context)

def main(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            send_email(name, email, message)

    context = {
        'title': 'It\'s me again!',
    }
    return render(request, 'main/main.html', context)

def main_ru(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            send_email(name, email, message)

    context = {
        'title': 'Это снова я!',
    }
    return render(request, 'main/main-ru.html', context)