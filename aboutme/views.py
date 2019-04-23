from django.shortcuts import render


def index(request):
    return render(request, 'aboutme/index.html', {})


def contact(request):
    return render(request, 'aboutme/contact.html', {})


def experiences(request):
    return render(request, 'aboutme/experiences.html', {})


def portofolio(request):
    return render(request, 'aboutme/portofolio.html', {})
