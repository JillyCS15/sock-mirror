from django.shortcuts import render


def pattern_page(request):
    return render(request, 'main/pattern-page.html')
