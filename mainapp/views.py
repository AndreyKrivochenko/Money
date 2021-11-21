from django.shortcuts import render
from common.constants import MAIN_MENU


def main_page(request):
    title = 'Главная'
    context = {
        'title': title,
        'main_menu': MAIN_MENU,
    }
    return render(request, 'mainapp/main_page.html', context)
