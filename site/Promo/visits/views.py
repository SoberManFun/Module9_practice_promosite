from django.shortcuts import render
from visits.models import Flat


def index(request):
    context = {
        'title': 'Сайт для ведения промо - компаний',
        'top_menu_username': 'Raider',
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
    }
    return render(request, 'visits/Index.html', context)


def visits_p(request):
    context = {
        'title': 'Сайт для ведения промо - компаний',
        'top_menu_username': 'Raider',
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
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

        'visits_list': [
            {
                'visit_list_n': 75,
                'house_list': 'Address_1',
                'flats_list_quant': 3,
                'date_list': '01.08.2023'

            },
            {
                'visit_list_n': 48,
                'house_list': 'Address_2',
                'flats_list_quant': 11,
                'date_list': '02.08.2023'

            },
            {
                'visit_list_n': 35,
                'house_list': 'Address_3',
                'flats_list_quant': 17,
                'date_list': '03.08.2023'

            },
            {
                'visit_list_n': 91,
                'house_list': 'Address_4',
                'flats_list_quant': 24,
                'date_list': '04.08.2023'

            }
        ],

        'houses_list': ['Дом_1', 'Дом_2', 'Дом_3', 'Дом_4', 'Дом_5', 'Дом_6', 'Дом_7', 'Дом_8', 'Дом_9']

    }
    return render(request, 'visits/visits_page.html', context)


def flats_p(request):
    context = {
        'title': 'Сайт для ведения промо - компаний',
        'top_menu_username': 'Raider',
        'top_menu_dashboard': 'Главная страница',
        'top_menu_reports': 'Отчеты',
        'top_menu_visits': 'ОБХОДЫ',
        'top_menu_accounts': 'Учетные записи',
        'top_menu_logout': 'Выйти',
        'top_menu_directories': 'Справочники',
        'top_menu_is_director': True,
        'top_menu_flats' : 'Справочник квартир',
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
