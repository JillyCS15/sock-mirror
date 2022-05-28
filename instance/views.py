from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PatternInstanceForm
from .models import SHACLPattern


def instance_page(request):
    # check if the user is admin
    is_admin = False
    if request.user.is_superuser:
        is_admin = True

    # Get Pattern Forms
    pattern_instance_form = PatternInstanceForm

    # Get all SHACL Patterns
    shacl_patterns = SHACLPattern.objects.all()
    shacl_pattern_dict = dict()
    for shacl_pattern in shacl_patterns:
        data = dict()
        data['description'] = shacl_pattern.description
        data['shacl_pattern'] = shacl_pattern.shacl_pattern
        shacl_pattern_dict[shacl_pattern.id] = data

    context = {
        "is_admin": is_admin,
        "pattern_instance_form": pattern_instance_form,
        "shacl_patterns": shacl_patterns,
        "shacl_patterns_data": shacl_pattern_dict,
        }
    return render(request, 'main/instance-page.html', context)


def add_pattern_instance(request):
    if request.method == "POST":
        form = PatternInstanceForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Successfully created a new pattern instance."
            messages.success(request, message)
            return redirect('instance:instance')
        message = "There is an error in data input."
        messages.error(request, message)
        return redirect('instance:instance')
    return redirect('instance:instance')
