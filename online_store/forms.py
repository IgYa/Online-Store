from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *

class GoodsNewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['goods_group'].empty_label = "Категория не выбрана"

    class Meta:
        model = Goods
        fields = ['name', 'slug', 'part_number', 'barcode', 'price', 'description', 'photo', 'is_active', 'is_hot', 'goods_group']
        # или указать fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
    # валидация поля name (должна быть не более 200 символов)
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Довжина перевищує 200 символів')

        return name


class OrderNewForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['goods_group'].empty_label = "Категория не выбрана"

    class Meta:
        model = OrderFilling
        fields = ['goods', 'amount', 'price_selling', 'total_price', 'order']
        # или указать fields = '__all__'
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-input'}),
        #     'description': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        # }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логін', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label="Ім'я", widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Прізвище', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор паролю', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

