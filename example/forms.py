from django import forms

from .models import BpmnTemplate
from bpmn_widget.widgets import BPMNWidget


class BpmnTemplateForm(forms.ModelForm):
    class Meta:
        model = BpmnTemplate
        widgets = {
            'content': BPMNWidget()
        }
        fields = '__all__'
