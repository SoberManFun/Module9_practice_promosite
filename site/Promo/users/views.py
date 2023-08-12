from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from visits.urls import index
from users.models import User
from users.forms import UserLoginForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('visits:index'))
    else:
        form = UserLoginForm()
    context = {
        'form': form,
        'title': 'Вход в систему',
        'title_box': 'Введите ваш логин/пароль',
        'label_login': 'Логин',
        'label_pass': 'Пароль',
        'button_enter': 'Вход',
        'bottom_register': 'Регистрация',

    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Регистрация нового пользователя',
        'table_title': 'Создание учетной записи',
        'table_first_name': 'Имя',
        'table_last_name': 'Фамилия',
        'table_email': 'Электронная почта',
        'table_phone': 'Номер телефона',
        'table_login': 'Логин',
        'table_pass': 'Пароль',
        'table_pass_confirm': 'Подтверждение пароля',
        'button_accept': 'Создание',
        'button_cancel': 'Отмена',
        'photo': 'Фотография',
        'button_photo': 'Выбрать',

        'top_menu_is_director': True,
    }
    return render(request, 'users/register.html', context)
