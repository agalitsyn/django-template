from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def page_not_found(request, exception):
    return render(request, 'main/404.html')


def server_error(request):
    return render(request, 'main/500.html')
