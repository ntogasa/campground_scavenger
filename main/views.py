from django.shortcuts import render


def about_view(request):
    return render(request, 'about.html')


def api_gateway_view(request):
    return render(request, 'api_gateway.html')