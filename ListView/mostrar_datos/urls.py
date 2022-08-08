from django.urls import path
from . import views
from mostrar_datos.views import datos_con_listview, books_and_categories


urlpatterns = [
    path('', views.index, name="index"),
    path('datos_con_listview/', datos_con_listview.as_view()),
    path('books_and_categories/', books_and_categories.as_view()),
]



