from django import forms


class BPMNWidget(forms.TextInput):
    template_name = 'django_bpmn_widget/bpmn.html'

    class Media:
        css = {
            'all':
                (
                    'django_bpmn_widget/bpmn-js/assets/diagram-js.css',
                    'django_bpmn_widget/bpmn-js/assets/bpmn-js.css',
                    'django_bpmn_widget/bpmn-js/assets/bpmn-font/css/bpmn-embedded.css',
                    'django_bpmn_widget/bpmn-js-properties-panel/assets/properties-panel.css'
                 ),
               }
        js = (
            'django_bpmn_widget/bpmn-integration-properties-panel.js',
        )
