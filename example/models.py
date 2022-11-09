from django.db import models


class BpmnTemplate(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField()