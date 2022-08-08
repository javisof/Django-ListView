from django.urls import path
from . import views
from show_data.views import data_with_listview, books_and_categories


urlpatterns = [
    path('', views.index, name="index"),
    path('data_with_listview/', data_with_listview.as_view()),
    path('books_and_categories/', books_and_categories.as_view()),
]



