from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control validate col-xl-9 col-lg-8 col-md-8 col-sm-7',
        'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control validate', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control validate', 'placeholder': 'Придумайте логин'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control validate', 'placeholder': 'Придумайте пароль', }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control validate', 'placeholder': 'Придумайте пароль', }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control validate', 'placeholder': 'Имя пользователя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control validate', 'placeholder': 'Фамилия пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control validate', 'placeholder': 'email пользователя '}))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control validate', 'placeholder': 'Телефон пользователя', 'type': 'number'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control validate', 'readonly': True}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'type': 'number'}))
   # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'btn'}), required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control validate', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username')
