from django.shortcuts import render
from .models import Book, Category
from django.views.generic import ListView


def index(request):
    books = Book.objects.all()

    context = {
        'books': books,
    }

    return render(request, 'index.html', context)


class data_with_listview(ListView):
    template_name = 'book-list.html'
    queryset = Book.objects.all()
    context_object_name = 'book'


class books_and_categories(ListView):
    template_name = 'book-list_with_categories.html'
    queryset = Book.objects.all()
    context_object_name = 'book'

    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    """
    def get_context_data(self, **kwargs):
        context = super(books_and_categories, self).get_context_data(**kwargs)
        #context['categories'] = self.object.book_set.all()
        #context['categories'] = Category.objects.filter(categories=self.categories)
        return context





