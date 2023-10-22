from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-5 px-8 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields =('category', 'name', 'descripion', 'price', 'image', )   
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'descripion': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }