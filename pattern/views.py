from django.shortcuts import render
from .models import ClassPattern, SHACLPattern


def pattern_page(request):
    # check if the user is admin
    is_admin = False
    if request.user.is_superuser:
        is_admin = True

    # query all pattern class and their SHACL patterns
    result_list = []
    pattern_list = ClassPattern.objects.all()
    for pattern in pattern_list:
        shacl_pattern = SHACLPattern.objects.filter(pattern_class_id=pattern.id)
        result_list.append([pattern, shacl_pattern])

    context = {
        "is_admin": is_admin,
        "patterns": result_list,
        }
    return render(request, 'main/pattern-page.html', context)
