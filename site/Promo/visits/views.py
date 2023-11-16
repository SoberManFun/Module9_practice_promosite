from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages
from django.urls import reverse
from django.db.models import Count, Case, When, IntegerField, F
from visits.models import Flat, FlatContact, House, Visit, Company, UserCompanies, CompaniesHouse, VisitFlat
from users.models import User
from visits.forms import FlatsAddForm, FlatsEditForm, FlatsContactEditForm, CompaniesEditForm, VisitsAddForm, \
    VisitsFlatsAddForm, \
    VisitsEditForm, VisitsFlatsEditForm, HousesAddForm, HousesEditForm, UserCompaniesForm, StatDoorForm, StatReactForm


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
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
        'top_menu_is_director': True,

    }
    return render(request, 'visits/Index.html', context)


def flats(request):
    if request.method == 'POST':
        form = FlatsAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новая квартира добавлена!')
            return HttpResponseRedirect(reverse('visits:flats_p'))
    else:
        form = FlatsAddForm()
    user = request.user
    context = {
        'form': form,
        'title': 'Справочник квартир',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
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
        'column_right_bot_button': 'Добавить дом',
        'Page_list': 'Страница',
        'flats_list': Flat.objects.order_by('Flat_House_Address'),
        'houses_list': House.objects.all()

    }
    return render(request, 'visits/flats_page.html', context)


def flats_edit(request, flat_id):
    user = request.user
    eflatid = Flat.objects.get(id=flat_id)
    if request.method == 'POST':
        flat_form = FlatsEditForm(request.POST, instance=eflatid)
        flatcontact_form = FlatsContactEditForm(request.POST)
        if flat_form.is_valid() and flatcontact_form.is_valid():
            flat = flat_form.save()
            flatcontact = flatcontact_form.save(commit=False)
            flatcontact.Flat = flat
            flatcontact.save()
            messages.success(request, 'Данные по квартире изменены!')
            # return redirect('edit_flats.html')   Перенаправление на страницу успешного сохранения
            # return HttpResponseRedirect(reverse('visits:flats_edit_p'))
    else:
        flat_form = FlatsEditForm(instance=eflatid)
        flatcontact_form = FlatsContactEditForm()
    eflatcontact = FlatContact.objects.filter(Flat_id=flat_id)
    context = {
        'flat': eflatid,
        'form': flat_form,
        'contact_form': flatcontact_form,
        'title': 'Справочник квартир',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'top_menu_flats': 'Справочник квартир',
        'table_column_top_name_1': 'Номер квартиры',
        'table_column_top_name_2': 'Дом',
        'table_column_top_name_3': 'Владелец',
        'contact_table_column_top_name_1': 'Имя',
        'contact_table_column_top_name_2': 'Телефон',
        'contact_table_column_top_name_3': 'Комментарий',
        'flat_contact_empty': 'Контактная информация не заполнена!',
        'FlatContact_Name_lbl': 'Имя',
        'FlatContact_Phone_lbl': 'Телефон',
        'FlatContact_Comment_lbl': 'Комментарий',
        'table_right_top_button': 'Добавить квартиру',
        'table_left_but_button': 'Удалить выбранные квартиры',
        'column_right_top_name': 'Контактная информация',
        'column_right_bot_button': '',
        'Page_list': 'Страница',
        'flats_list': Flat.objects.order_by('Flat_House_Address'),
        'flatscontact_list': eflatcontact

    }
    return render(request, 'visits/flats_edit_page.html', context)


def flat_contact_add(request, flat_id):
    vflatid = Flat.objects.get(id=flat_id)
    contform = FlatsContactEditForm(request.POST)
    if contform.is_valid():
        vflatcontact = contform.save(commit=False)
        vflatcontact.Flat = vflatid
        vflatcontact.save()
    eflatcontact = FlatContact.objects.filter(Flat_id=flat_id)
    context = {
        'flat': vflatid,
        'form_contact': contform,
        'flatscontact_list': eflatcontact,
        'contact_table_column_top_name_1': 'Имя',
        'contact_table_column_top_name_2': 'Телефон',
        'contact_table_column_top_name_3': 'Комментарий',
    }
    return HttpResponseRedirect(request.META['HTTP_REFERER'], context)


def houses(request):
    user = request.user
    if request.method == 'POST':
        form = HousesAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новый дом добавлен!')
            return HttpResponseRedirect(reverse('visits:houses_p'))
    else:
        form = HousesAddForm()
        # companieshouse = CompaniesHouse.objects.filter(UserCompanies_User=user)
    context = {
        'form': form,
        'title': 'Справочник домов',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'top_menu_flats': 'Справочник домов',
        'table_column_top_name_1': 'Адрес',
        'table_column_top_name_2': 'Номер дома',
        'table_column_top_name_3': 'Этажность',
        'table_column_top_name_4': 'Количество подъездов',
        'table_column_top_name_5': 'Количество квартир',
        'table_right_top_button': 'Добавить дом Копка',
        'table_left_but_button': 'Удалить выбранный дом',
        'column_right_top_name': 'Список квартир',
        'column_right_bot_button': 'Добавить новую квартиру',
        'Page_list': 'Страница',
        'houses_list': House.objects.all(),
        'flats_list': Flat.objects.all(),
        'houses_table_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/houses_page.html', context)


def houses_edit(request, house_id):
    user = request.user
    ehouseid = House.objects.get(id=house_id)
    if request.method == 'POST':
        house_form = HousesEditForm(request.POST, instance=ehouseid)
        if house_form.is_valid():
            house_form.save()
            messages.success(request, 'Дом изменен!')
    else:
        house_form = HousesEditForm(instance=ehouseid)
    context = {
        'form': house_form,
        'title': 'Справочник домов',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'top_menu_flats': 'Справочник домов',
        'table_column_top_name_1': 'Адрес',
        'table_column_top_name_2': 'Номер дома',
        'table_column_top_name_3': 'Этажность',
        'table_column_top_name_4': 'Количество подъездов',
        'table_column_top_name_5': 'Количество квартир',
        'table_right_top_button': 'Добавить дом Копка',
        'table_left_but_button': 'Удалить выбранный дом',
        'column_right_top_name': 'Список квартир',
        'column_right_bot_button': 'Добавить новую квартиру',
        'Page_list': 'Страница',
        'flathouseid': ehouseid,
        'houses_list': House.objects.all(),
        'flats_list': Flat.objects.all(),
        'houses_table_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/houses_edit_page.html', context)


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
    usercompanies = UserCompanies.objects.filter(UserCompanies_User=user)
    usercompfiltercount = usercompanies.count()
    if request.method == 'POST':
        form = CompaniesEditForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новая компания добавлена!')
            return HttpResponseRedirect(reverse('visits:companies_p'))
    else:
        form = CompaniesEditForm()
    context = {
        'form': form,
        'companies': comp,
        'usercompanies_list': usercompanies,
        'ucfcount': usercompfiltercount,
        'title': 'Справочник компаний',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
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


def usercompanyadd(request, company_id):
    companies = Company.objects.all()
    company = Company.objects.get(id=company_id)
    usercompanies = UserCompanies.objects.filter(UserCompanies_User=request.user, UserCompanies_Company=company)
    if not usercompanies.exists():
        UserCompanies.objects.create(UserCompanies_User=request.user, UserCompanies_Company=company)
    else:
        messages.error(request, 'Сотрудник уже привязан к данной компании')
    context = {
        'companies': companies,
    }
    return HttpResponseRedirect(request.META['HTTP_REFERER'], context)


def visits(request):
    user = request.user
    context = {
        'title': 'ОБХОДЫ',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
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
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
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


def edit_visit(request, visit_id):
    user = request.user
    editvisitid = Visit.objects.get(id=visit_id)
    editvisitflatid = VisitFlat.objects.get(VisitFlat_Visit=visit_id)
    if request.method == 'POST':
        visit_form = VisitsEditForm(request.POST, instance=editvisitid)
        flat_form = VisitsFlatsEditForm(request.POST, instance=editvisitflatid)
        if visit_form.is_valid() and flat_form.is_valid():
            visit = visit_form.save(commit=False)
            visit.User = user  # Присваиваем текущего пользователя полю user
            visit.save()
            vflat = flat_form.save(commit=False)
            vflat.VisitFlat_Visit = visit
            vflat.save()
            messages.success(request, 'Обход изменен!')

    else:
        visit_form = VisitsEditForm(instance=editvisitid)
        flat_form = VisitsFlatsEditForm(instance=editvisitflatid)

    context = {
        'form': visit_form,
        'flat_form': flat_form,
        'title': 'Справочник компаний',
        'top_menu_username': user,
        'top_menu_userid': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
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
        'table_right_top_button': 'Сохранить обход',
        'table_left_but_button': '',
        'column_right_top_name': 'Дома компании',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'houses_table_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/edit_visit_page.html', context)


def statistics_door(request):
    user = request.user
    company = request.POST.get('Visit_Company')
    house = request.POST.get('Visit_House')
    door = request.POST.get('Visit_Door')
    total_visits = Visit.objects.filter(Visit_Company=company).count()
    total_open_doors = Visit.objects.filter(Visit_Company=company, Visit_Door='True').count()
    total_closed_doors = Visit.objects.filter(Visit_Company=company, Visit_Door='False').count()

    if house == '':
        companyform = StatDoorForm(request.POST)
        visitsfilter = Visit.objects.filter(Visit_Company=company, Visit_Door=door)
    else:
        companyform = StatDoorForm(request.POST)
        visitsfilter = Visit.objects.filter(Visit_Company=company, Visit_House=house, Visit_Door=door)

    if total_visits != 0 and total_open_doors != 0 and total_closed_doors != 0:
        overall_open_percentage = round(((total_open_doors / total_visits) * 100))
        overall_closed_percentage = round(((total_closed_doors / total_visits) * 100))
        house_wise_data = Visit.objects.filter(Visit_Company=company).values('Visit_House').annotate(
            open_doors=Count(Case(When(Visit_Door='True', then=1), output_field=IntegerField())),
            closed_doors=Count(Case(When(Visit_Door='False', then=1), output_field=IntegerField())))
        data_list = []
        for data in house_wise_data:
            data_list.append({'House': data['Visit_House'],
                              'Open': round(((data['open_doors'] / (data['open_doors'] + data['closed_doors'])) * 100)),
                              'Closed': round(((data['closed_doors'] / (data['open_doors'] + data['closed_doors'])) * 100))})
    else:
        overall_open_percentage = 0
        overall_closed_percentage = 0
        data_list = []

    context = {
        'form': companyform,
        'title': 'СТАТИСТИКА по ДВЕРЯМ',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
        'top_menu_accounts': 'Учетная запись',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'table_column_top_name_1': 'Номер обхода',
        'table_column_top_name_2': 'Дата обхода',
        'table_column_top_name_3': 'Время обхода',
        'table_column_top_name_4': 'Дом',
        'table_column_top_name_5': 'Компания',
        'table_right_top_button': 'Показать',
        'table_left_but_button': 'Удалить выбранные обходы',
        'column_right_top_name': 'Список домов',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'visits_list': visitsfilter,
        'overall_open_percentage': overall_open_percentage,
        'overall_closed_percentage': overall_closed_percentage,
        'house_wise_data': data_list,

    }
    return render(request, 'visits/stat_door_page.html', context)


def statistics_reaction(request):
    user = request.user
    company = request.POST.get('Visit_Company')
    house = request.POST.get('Visit_House')
    react = request.POST.get('Visit_Reaction')
    total_visits = Visit.objects.filter(Visit_Company=company).count()
    total_pos_react = Visit.objects.filter(Visit_Company=company, Visit_Reaction='1').count()
    total_neutral_react = Visit.objects.filter(Visit_Company=company, Visit_Reaction='2').count()
    total_neg_react = Visit.objects.filter(Visit_Company=company, Visit_Reaction='3').count()
    total_no_react = Visit.objects.filter(Visit_Company=company, Visit_Reaction='4').count()

    if house == '':
        companyform = StatReactForm(request.POST)
        visitsfilter = Visit.objects.filter(Visit_Company=company, Visit_Reaction=react)
    else:
        companyform = StatReactForm(request.POST)
        visitsfilter = Visit.objects.filter(Visit_Company=company, Visit_House=house, Visit_Reaction=react)

    if total_visits != 0 and total_no_react:
        overall_pos_percentage = round(((total_pos_react / total_visits) * 100))
        overall_neutral_percentage = round(((total_neutral_react / total_visits) * 100))
        overall_neg_percentage = round(((total_neg_react / total_visits) * 100))
        house_wise_data = Visit.objects.filter(Visit_Company=company).values('Visit_House').annotate(
            pos_react=Count(Case(When(Visit_Reaction='1', then=1), output_field=IntegerField())),
            neutral_react=Count(Case(When(Visit_Reaction='2', then=1), output_field=IntegerField())),
            neg_react=Count(Case(When(Visit_Reaction='3', then=1), output_field=IntegerField())),
            no_react=Count(Case(When(Visit_Reaction='4', then=1), output_field=IntegerField())))
        print(house_wise_data)
        data_list = []
        for data in house_wise_data:
            if data['no_react'] == 0:
                data_list.append({'House': data['Visit_House'],
                                  'Positive': round(((data['pos_react'] / (data['pos_react'] + data['neutral_react'] + data['neg_react'])) * 100)),
                                  'Neutral': round(((data['neutral_react'] / (data['pos_react'] + data['neutral_react'] + data['neg_react'])) * 100)),
                                  'Negative': round(((data['neg_react'] / (data['pos_react'] + data['neutral_react'] + data['neg_react'])) * 100))})
    else:
        overall_pos_percentage = 0
        overall_neutral_percentage = 0
        overall_neg_percentage = 0
        data_list = []

    context = {
        'form': companyform,
        'title': 'СТАТИСТИКА по РЕАКЦИЯМ',
        'top_menu_username': user,
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_reports_door': 'Статистика по дверям',
        'top_menu_reports_reaction': 'Статистика по реакциям',
        'top_menu_reports_contacts': 'Статистика по контактам',
        'top_menu_accounts': 'Учетная запись',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'table_column_top_name_1': 'Номер обхода',
        'table_column_top_name_2': 'Дата обхода',
        'table_column_top_name_3': 'Время обхода',
        'table_column_top_name_4': 'Дом',
        'table_column_top_name_5': 'Компания',
        'table_right_top_button': 'Показать',
        'table_left_but_button': 'Удалить выбранные обходы',
        'column_right_top_name': 'Список домов',
        'column_right_bot_button': 'Добавить новый дом',
        'Page_list': 'Страница',
        'visits_list': visitsfilter,
        'overall_pos_percentage': overall_pos_percentage,
        'overall_neutral_percentage': overall_neutral_percentage,
        'overall_neg_percentage': overall_neg_percentage,
        'house_wise_data': data_list,

    }
    return render(request, 'visits/stat_reaction_page.html', context)

