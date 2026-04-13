from django import forms
from django.core.exceptions import ValidationError


class NameForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'})
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.strip():
            raise ValidationError('Поле имени не может состоять только из пробелов.')
        return name
