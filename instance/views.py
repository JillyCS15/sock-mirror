from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PatternInstanceForm
from .models import SHACLPattern, PatternInstance
# from rdflib import Graph


def instance_page(request):
    # check if the user is admin
    is_admin = False
    if request.user.is_superuser:
        is_admin = True

    # Get Pattern Forms
    pattern_instance_form = PatternInstanceForm

    query = request.GET.get('query', '')
    pattern_instances = PatternInstance.objects.filter(name__icontains=query)

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
        "pattern_instances": pattern_instances,
        "query": query,
        }
    return render(request, 'main/instance-page.html', context)


def add_pattern_instance(request):
    if request.method == "POST":
        form = PatternInstanceForm(request.POST)
        if form.is_valid():
            try:
                # shacl_shapes = form.cleaned_data['shacl_shapes']
                # Graph().parse(data=shacl_shapes)
                form.save()
                message = "Successfully created a new pattern instance."
                messages.success(request, message)
                return redirect('instance:instance')
            except:
                message = "Invalid SHACL shapes!"
                messages.error(request, message)
                return redirect('instance:instance')
        message = "There is an error in data input."
        messages.error(request, message)
        return redirect('instance:instance')
    return redirect('instance:instance')


def show_pattern_instance_detail(request, pattern_instance_id):
    pattern_instance = PatternInstance.objects.get(id=pattern_instance_id)
    context = {
        "pattern_instance": pattern_instance,
        }
    return render(request, 'main/instance-detail-page.html', context)


def download_pattern_instance(request, pattern_instance_id):
    pattern_instance = PatternInstance.objects.get(id=pattern_instance_id)

    response = HttpResponse(pattern_instance.shacl_shapes, content_type='text/plain')
    filename = f"{pattern_instance.name}-shapes.ttl"
    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response
