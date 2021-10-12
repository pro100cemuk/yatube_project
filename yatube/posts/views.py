from django.http import HttpResponse

# Главная страница
def index(request):
    return HttpResponse('Главная страница блогеров')

# Страница со постами, отфильтрованными по группам
def group_posts(request, group_name):
    return HttpResponse(f'Посты группы {group_name}')