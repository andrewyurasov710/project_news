from django import forms

from .models import News, Category


class NewsForm(forms.ModelForm):
    # title = forms.CharField(max_length=150, label='Назва', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'rows': 6,
    # }))
    # is_published = forms.BooleanField(label='Опубліковано', initial=True)
    # category = forms.ModelChoiceField(empty_label='Обери категорію', label='Категорія', queryset=Category.objects.all(),
    #                                   widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
