from django.shortcuts import render

from example.forms import BpmnTemplateForm


def index(request):
    formset = BpmnTemplateForm()
    return render(request, 'index.html', {'formset': formset})
