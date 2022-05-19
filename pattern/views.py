from django.shortcuts import render
from .models import SHACLPattern


def pattern_page(request):
    is_admin = False
    if request.user.is_superuser:
        is_admin = True
    context = {
        "is_admin": is_admin,
        "patterns": SHACLPattern.objects.all(),
        }
    return render(request, 'main/pattern-page.html', context)
