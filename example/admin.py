from django.contrib import admin

from .models import BpmnTemplate
from .forms import BpmnTemplateForm


class BpmnTemplateAdmin(admin.ModelAdmin):
    form = BpmnTemplateForm

admin.site.register(BpmnTemplate, BpmnTemplateAdmin)
