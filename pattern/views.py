from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClassPatternForm, SHACLPatternForm
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

    # Get Pattern Forms
    class_pattern_form = ClassPatternForm
    shacl_pattern_form = SHACLPatternForm

    context = {
        "is_admin": is_admin,
        "patterns": result_list,
        "class_pattern_form": class_pattern_form,
        "shacl_pattern_form": shacl_pattern_form
        }
    return render(request, 'main/pattern-page.html', context)


def add_class_pattern(request):
    if request.method == "POST":
        form = ClassPatternForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Successfully created a new class pattern."
            messages.success(request, message)
            return redirect('pattern:pattern')
        message = "There is an error in data input."
        messages.error(request, message)
        return redirect('pattern:pattern')
    return redirect('pattern:pattern')


def add_shacl_pattern(request):
    if request.method == "POST":
        form = SHACLPatternForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Successfully created a new class pattern."
            messages.success(request, message)
            return redirect('pattern:pattern')
        message = "There is an error in data input."
        messages.error(request, message)
        return redirect('pattern:pattern')
    return redirect('pattern:pattern')


def delete_class_pattern(request, class_pattern_id):
    class_pattern = ClassPattern.objects.get(id=class_pattern_id)
    message = f"{class_pattern.name} has been deleted."
    class_pattern.delete()
    messages.error(request, message)
    return redirect('pattern:pattern')


def delete_shacl_pattern(request, shacl_pattern_id):
    shacl_pattern = SHACLPattern.objects.get(id=shacl_pattern_id)
    message = f"{shacl_pattern.pattern_class.name} with ID {shacl_pattern.code} has been deleted."
    shacl_pattern.delete()
    messages.error(request, message)
    return redirect('pattern:pattern')
