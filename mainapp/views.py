from django.shortcuts import render


def main_page(request):
    title = 'Main'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/main_page.html', context)
