from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со постами, отфильтрованными по группам
    path('groups/<slug:group_name>/', views.group_posts),
]