# -*- coding: utf-8 -*-
from django.forms import ModelForm, Select, TextInput, NumberInput
from .models import Kt, BjjydyArticle

class BjjydyArticleForm(ModelForm):
    class Meta:
        model = BjjydyArticle
        exclude = []

class KtForm(ModelForm):
    class Meta:
        model = Kt
        exclude = []
        widgets = {
            'year': NumberInput(attrs={'class': 'input-text'}),
            'kt_type': Select(attrs={'class':'select'}),
            'project_number': TextInput(attrs={'class': 'input-text'}),
            'applicant': TextInput(attrs={'class': 'input-text'}),
            'school': TextInput(attrs={'class': 'input-text'}),
            'kt_name': TextInput(attrs={'class': 'input-text'}),
            'is_completed_or_not': Select(attrs={'class':'select'}),
            'remark': TextInput(attrs={'class': 'input-text'}),
        }
