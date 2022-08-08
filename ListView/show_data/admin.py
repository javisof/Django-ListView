from django.contrib import admin
from .models import Book, Category

# Register models in Admin Panel
admin.site.register(Book)
admin.site.register(Category)
