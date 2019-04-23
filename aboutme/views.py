from django.shortcuts import render


def index(request):
    return render(request, 'aboutme/index.html', {})


def contact(request):
    return render(request, 'aboutme/contact.html', {})
