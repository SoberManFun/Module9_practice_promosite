from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from visits.models import Flat, House, Visit, Company, UserCompanies, CompaniesHouse, VisitFlat
from users.models import User
from visits.forms import FlatsEditForm, CompaniesEditForm, VisitsAddForm, VisitsFlatsAddForm, VisitsEditForm, \
    VisitsFlatsEditForm
from django.http import JsonResponse


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


def flats(request):
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


def houses(request):
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


def houses_card(request):
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


def companies(request):
    user = request.user
    comp = Company.objects.all()
    if request.method == 'POST':
        form = CompaniesEditForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новая компания добавлена!')
            return HttpResponseRedirect(reverse('visits:companies_p'))
    else:
        form = CompaniesEditForm()
        usercompanies = UserCompanies.objects.filter(UserCompanies_User=user)
    context = {
        'form': form,
        'companies': comp,
        'usercompanies_list': usercompanies,
        'title': 'Справочник компаний',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'column_left_top_name': 'Сотрудники',
        'top_menu_flats': 'Справочник компаний',
        'table_column_top_name_1': 'Наименование',
        'table_column_top_name_2': 'Адрес',
        'table_column_top_name_3': 'Директор',
        'table_column_top_name_4': 'ИНН',
        'table_column_top_name_5': '',
        'table_right_top_button': 'Добавить компанию',
        'table_left_but_button': 'Удалить выбранную компанию',
        'column_right_top_name': 'Дома компании',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'companies_list': Company.objects.all(),
        'houses_list': House.objects.all(),
        'companieshouse_list': CompaniesHouse.objects.all(),
        'houses_table_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/companies_page.html', context)


def visits(request):
    user = request.user
    context = {
        'title': 'ОБХОДЫ',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетная запись',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'table_column_top_name_1': 'Номер обхода',
        'table_column_top_name_2': 'Дата обхода',
        'table_column_top_name_3': 'Время обхода',
        'table_column_top_name_4': 'Дом',
        'table_column_top_name_5': 'Сотрудник',
        'table_right_top_button': 'Добавить обход',
        'table_left_but_button': 'Удалить выбранные обходы',
        'column_right_top_name': 'Список домов',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'visits_list': Visit.objects.all(),
        'houses_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/visits_page.html', context)


def add_visit(request):
    user = request.user
    if request.method == 'POST':
        visit_form = VisitsAddForm(request.POST)
        flat_form = VisitsFlatsAddForm(request.POST)
        if visit_form.is_valid() and flat_form.is_valid():
            visit = visit_form.save(commit=False)
            visit.User = user  # Присваиваем текущего пользователя полю user
            visit.save()
            vflat = flat_form.save(commit=False)
            # flat_numbers = vflat.cleaned_data['VisitFlat_Flat'].split()  # Разделение введенных номеров квартир по пробелу
            # for flat_number in flat_numbers:
            #     VisitFlat.objects.create(VisitFlat_Visit=visit, VisitFlat_Flat=flat_number)
            # return visit
            vflat.VisitFlat_Visit = visit
            vflat.save()
            messages.success(request, 'Новый обход добавлен!')
            # return redirect('edit_flats.html')   Перенаправление на страницу успешного сохранения
            # return HttpResponseRedirect(reverse('visits:add_visit_p'))
    else:
        visit_form = VisitsAddForm()
        flat_form = VisitsFlatsAddForm()

    context = {
        'form': visit_form,
        'flat_form': flat_form,
        'title': 'Справочник компаний',
        'top_menu_username': user,
        'top_menu_userid': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'Visit_Num_lbl': '№ Обхода',
        'Visit_Date_lbl': 'Дата обхода',
        'Visit_Time_lbl': 'Время обхода',
        'Visit_Company_lbl': 'Компания',
        'Visit_Employee_lbl': 'Сотрудник',
        'Visit_House_lbl': 'Дом',
        'Visit_Door_lbl': 'Дверь',
        'Visit_Reaction_lbl': 'Реакция',
        'VisitFlat_Flat_lbl': '№ квартиры',
        'top_menu_flats': 'Справочник компаний',
        'table_column_top_name_1': 'Наименование',
        'table_column_top_name_2': 'Адрес',
        'table_column_top_name_3': 'Директор',
        'table_column_top_name_4': 'ИНН',
        'table_column_top_name_5': '',
        'table_right_top_button': 'Добавить обход',
        'table_left_but_button': 'Удалить выбранную компанию',
        'column_right_top_name': 'Дома компании',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'houses_table_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/add_visit_page.html', context)


def edit_visit(request, visit_num):
    user = request.user
    editvisitnum = Visit.objects.get(Visit_Num=visit_num)
    if request.method == 'POST':
        visit_form = VisitsEditForm(request.POST, instance=editvisitnum)
        flat_form = VisitsFlatsEditForm(request.POST, instance=editvisitnum)
        if visit_form.is_valid() and flat_form.is_valid():
            visit = visit_form.save(commit=False)
            visit.User = user  # Присваиваем текущего пользователя полю user
            visit.save()
            vflat = flat_form.save(commit=False)
            vflat.VisitFlat_Visit = visit
            vflat.save()
            messages.success(request, 'Обход изменен!')

    else:
        visit_form = VisitsEditForm(instance=editvisitnum)
        flat_form = VisitsFlatsEditForm(instance=editvisitnum)

    context = {
        'form': visit_form,
        'flat_form': flat_form,
        'title': 'Справочник компаний',
        'top_menu_username': user,
        'top_menu_userid': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'Visit_Num_lbl': '№ Обхода',
        'Visit_Date_lbl': 'Дата обхода',
        'Visit_Time_lbl': 'Время обхода',
        'Visit_Company_lbl': 'Компания',
        'Visit_Employee_lbl': 'Сотрудник',
        'Visit_House_lbl': 'Дом',
        'Visit_Door_lbl': 'Дверь',
        'Visit_Reaction_lbl': 'Реакция',
        'VisitFlat_Flat_lbl': '№ квартиры',
        'top_menu_flats': 'Справочник компаний',
        'table_column_top_name_1': 'Наименование',
        'table_column_top_name_2': 'Адрес',
        'table_column_top_name_3': 'Директор',
        'table_column_top_name_4': 'ИНН',
        'table_column_top_name_5': '',
        'table_right_top_button': 'Просмотр/Изменение обхода',
        'table_left_but_button': '',
        'column_right_top_name': 'Дома компании',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'houses_table_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/edit_visit_page.html', context)
