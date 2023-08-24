from django.shortcuts import render

def index(request):
    data = {
        'title': 'Что это за сайт?'
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')