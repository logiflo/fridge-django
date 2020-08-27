from django import forms
from django.db import models

from .models import Food, Essencial

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['text', 'units', 'quantity']
        labels ={'text': 'Grocery',}


class QuantityForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['quantity']
        labels ={'quantity': '',}

class EssencialForm(forms.ModelForm):
    class Meta:
        model = Essencial
        fields = ['text', 'units', 'quantity']
        labels ={'text': 'Grocery',}


class QuantityEssencialForm(forms.ModelForm):
    class Meta:
        model = Essencial
        fields = ['quantity']
        labels ={'quantity': '',}