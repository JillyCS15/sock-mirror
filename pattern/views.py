from django.shortcuts import render


def pattern_page(request):
    is_admin = False
    if request.user.is_superuser:
        is_admin = True
    context = {
        "is_admin": is_admin,
        }
    return render(request, 'main/pattern-page.html', context)
