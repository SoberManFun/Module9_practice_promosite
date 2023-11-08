from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User
from visits.models import Flat, House, Visit, Company, UserCompanies, CompaniesHouse
from visits.forms import UserCompaniesForm

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
        'report_box': 'Неверный логин/пароль',
        'label_login': 'Логин',
        'label_pass': 'Пароль',
        'button_enter': 'Вход',
        'bottom_register': 'Регистрация',
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('users:login_p'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Регистрация нового пользователя',
        'table_title': 'Создание учетной записи',
        'table_first_name': 'Имя',
        'table_last_name': 'Фамилия',
        'table_email': 'Электронная почта',
        'table_phone': 'Номер телефона',
        'table_login': 'Логин',
        'table_pass': 'Пароль',
        'table_pass_confirm': 'Подтверждение пароля',
        'button_accept': 'Сохранить',
        'button_cancel': 'Отмена',
        'photo': 'Фотография',
        'button_photo': 'Выбрать',
        'top_menu_is_director': True,
    }
    return render(request, 'users/register.html', context)


def profile(request):
    user = request.user
    companies = Company.objects.all()
    vuserid = User.objects.get(username=user).id
    usrcomp = UserCompanies.objects.filter(UserCompanies_User=user)
    usercompform = UserCompaniesForm()
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile_p'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'vformuserid': vuserid,
        'form': form,
        'usrcompform': usercompform,
        'title': 'Страница учетной записи пользователя',
        'table_title': 'Просмотр учетной записи',
        'table_first_name': 'Имя',
        'table_last_name': 'Фамилия',
        'table_email': 'Электронная почта',
        'table_phone': 'Номер телефона',
        'table_login': 'Логин',
        'table_pass': '',
        'table_pass_confirm': '',
        'button_accept': 'Сохранить',
        'button_cancel': 'Отмена',
        'button_add': 'Добавить',
        'photo': 'Фотография',
        'button_photo': 'Выбрать',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетная запись',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'table_column_top_name_1': 'Наименование',
        'table_column_top_name_2': 'Адрес',
        'table_column_top_name_3': 'Директор',
        'table_column_top_name_4': 'ИНН',
        'companies_list': Company.objects.all(),
        'houses_list': House.objects.all(),
        'companieshouse_list': CompaniesHouse.objects.all(),
        'companies': companies,
        'usercompanies_list': usrcomp
    }
    return render(request, 'users/profile.html', context)


def profile_usercompanyadd(request):
    vuserid = request.user
    usercompform = UserCompaniesForm(request.POST)
    # if usercompform.is_valid():
    company_name = usercompform.cleaned_data['Companies']
    company_id = Company.objects.get(Company_Name=company_name)
    # vusercomp = usercompform.save(commit=False)
    vusercomp = UserCompanies(UserCompanies_User=vuserid, UserCompanies_Company=company_id)
    # vusercomp.UserCompanies_Company = company_id
    vusercomp.save()
    context = {
        'compname': company_name,
        'contact_table_column_top_name_1': 'Имя',
        'contact_table_column_top_name_2': 'Телефон',
        'contact_table_column_top_name_3': 'Комментарий',
    }
    return HttpResponseRedirect(request.META['HTTP_REFERER'], context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('users:login_p'))
