from django.shortcuts import render


def instance_page(request):
    return render(request, 'main/instance-page.html')
