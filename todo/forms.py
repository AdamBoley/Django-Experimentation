# This file handles form validation

from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']



# ItemForm is a class and inherits all of the functionality of the pre-built ModelForm from forms
# Meta is an inner class
# 