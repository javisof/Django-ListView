from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category)


    def __unicode__(self):
        return self.name








