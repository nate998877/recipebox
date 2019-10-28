from django.shortcuts import render

from recipebox.models import Recipe, CookBook, BookDistributor

def index(request):
    html = "index.html"
    recipes = "recipes.html"
    distributors = "recipes.html"
    books = "books.html"

    news = CookBook.objects.all()

    return render(request, [html, recipes, distributors, books], {"data": news})
