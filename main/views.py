from django.shortcuts import render

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
    context = {
        'title': 'It\'s me again!',
    }
    return render(request, 'main/main.html', context)

def main_ru(request):
    context = {
        'title': 'Это снова я!',
    }
    return render(request, 'main/main-ru.html', context)