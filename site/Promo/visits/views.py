from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.urls import reverse
from visits.models import Flat, House, Visit, Company, UserCompanies, CompaniesHouse
from visits.forms import FlatsEditForm
from users.models import User


def index(request):
    user = request.user
    context = {
        'title': 'Сайт для ведения промо - компаний',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетная запись',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
    }
    return render(request, 'visits/Index.html', context)


def visits_p(request):
    user = request.user
    context = {
        'title': 'Сайт для ведения промо - компаний',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетная запись',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'table_column_top_name_1': 'Номер обхода',
        'table_column_top_name_2': 'Дом',
        'table_column_top_name_3': 'Количество квартир',
        'table_column_top_name_4': 'Дата обхода',
        'table_right_top_button': 'Добавить обход',
        'table_left_but_button': 'Удалить выбранные обходы',
        'column_right_top_name': 'Список домов',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'visits_list': Visit.objects.all(),
        'houses_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/visits_page.html', context)


def flats_p(request):
    if request.method == 'POST':
        form = FlatsEditForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новая квартира добавлена!')
            # return redirect('edit_flats.html')   Перенаправление на страницу успешного сохранения
            return HttpResponseRedirect(reverse('visits:flats_p'))
    else:
        form = FlatsEditForm()
    user = request.user
    context = {
        'form': form,
        'title': 'Сайт для ведения промо - компаний',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'top_menu_flats': 'Справочник квартир',
        'table_column_top_name_1': 'Номер квартиры',
        'table_column_top_name_2': 'Дом',
        'table_column_top_name_3': 'Владелец',
        'table_column_top_name_4': '',
        'table_right_top_button': 'Добавить квартиру',
        'table_left_but_button': 'Удалить выбранные квартиры',
        'column_right_top_name': 'Список домов',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'flats_list': Flat.objects.all(),
        'houses_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/flats_page.html', context)


def houses_p(request):
    user = request.user
    context = {
        'title': 'Сайт для ведения промо - компаний',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'top_menu_flats': 'Справочник квартир',
        'table_column_top_name_1': 'Адрес',
        'table_column_top_name_2': 'Номер дома',
        'table_column_top_name_3': 'Этажность',
        'table_column_top_name_4': 'Количество подъездов',
        'table_column_top_name_5': 'Количество квартир',
        'table_right_top_button': 'Добавить дом',
        'table_left_but_button': 'Удалить выбранный дом',
        'column_right_top_name': 'Список квартир',
        'column_right_bot_button': 'Добавить новую квартиру',
        'Page_list': 'Страница',
        'houses_list': House.objects.all(),
        'flats_list': Flat.objects.all(),
        'houses_table_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/houses_page.html', context)


def houses_card_p(request):
    user = request.user
    context = {
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
    }
    return render(request, 'visits/houses_add_page.html', context)


def companies_p(request):
    user = request.user
    activeuser = User.objects.get(username=user)  # Замените <user_id> на идентификатор пользователя, которого выбираете
    companies = UserCompanies.objects.filter(UserCompanies_User=activeuser)
    company_filter = Company.objects.filter(id__in=companies)
    context = {
        'company_filter': company_filter,
        'title': 'Справочник компаний',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'column_left_top_name': 'Связанный пользователь',
        'top_menu_flats': 'Справочник кампаний',
        'table_column_top_name_1': 'Наименование',
        'table_column_top_name_2': 'Адрес',
        'table_column_top_name_3': 'Директор',
        'table_column_top_name_4': '',
        'table_column_top_name_5': '',
        'table_right_top_button': 'Добавить компанию',
        'table_left_but_button': 'Удалить выбранную компанию',
        'column_right_top_name': 'Список домов',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'companies_list': Company.objects.all(),
        'houses_list': House.objects.all(),
        'usercompanies_list': UserCompanies.objects.all(),
        'companieshouse_list': CompaniesHouse.objects.all(),
        'houses_table_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/companies_page.html', context)
