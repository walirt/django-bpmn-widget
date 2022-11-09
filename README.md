# django-bpmn-widget ![](https://img.shields.io/badge/language-Python3-brightgreen.svg)
django bpmn modeler widget(integrated with properties panel)

## Usage
1. Install django-bpmn-widget
```shell
pip install django-bpmn-widget
```
2. Add `bpmn_widget` to `settings.py` `INSTALLED_APPS`, like this:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bpmn_widget'
]
```
3. Display in Form
```python
from django import forms

from yourapp.models import MyModel
from bpmn_widget.widgets import BPMNWidget # import widget


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        widgets = {
            'content': BPMNWidget() # change it to the field you want to display
        }
        fields = '__all__'
```
4. Display in Django-Admin
```python
from django.contrib import admin

from yourapp.models import MyModel
from yourapp.forms import MyModelForm


class MyModelAdmin(admin.ModelAdmin):
    form = MyModelForm

admin.site.register(MyModel, MyModelAdmin)
```

## Note
The following is the js library for widget integration
- bpmn-js@10.2.1
- bpmn-js-properties-panel@1.10.0
- camunda-bpmn-moddle@7.0.1

If you want to update their version or extend other plug-ins, please compile them yourself

## Screenshot
![img.png](https://github.com/walirt/django-bpmn-widget/blob/main/screenshot/img.png?raw=true)


## Reference
[bpmn-js](https://github.com/bpmn-io/bpmn-js)  
[django-bpmn](https://github.com/jplobianco/django-bpmn)  


# License
![](https://img.shields.io/badge/License-MIT-blue.svg)
