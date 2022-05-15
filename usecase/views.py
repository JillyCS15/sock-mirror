from django.shortcuts import render


def usecase_page(request):
    return render(request, 'main/usecase-page.html')
