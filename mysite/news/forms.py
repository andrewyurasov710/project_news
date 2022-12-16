from django import forms

from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Назва', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 6,
    }))
    is_published = forms.BooleanField(label='Опубліковано', initial=True)
    category = forms.ModelChoiceField(empty_label='Обери категорію', label='Категорія', queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    
