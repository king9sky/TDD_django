#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Marvin King
# Date     : 2019-02-25 
from django import forms
from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"
# class ItemForm(forms.Form):
#     item_text = forms.CharField()
#     widget = forms.fields.TextInput(attrs={
#         'placeholder': 'Enter a to-do item',
#         'class':'form-control input-lg'
#     })

class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item  # 指定表单应用模型
        fields = ('text',)  # 使用字段
        widgets = {
            'text': forms.fields.TextInput(
                attrs={
                    'placeholder': 'Enter a to-do item',
                    'class': 'form-control input-lg',
                }
            ),
        }
        error_messages = {
            'text':{'required':EMPTY_ITEM_ERROR}
        }
