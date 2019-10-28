from django.shortcuts import render

from recipebox.models import Recipe, CookBook, BookDistributor

def index(request):
    html = "index.html"

    return render(request, html)


def recipes(request):
    recipes = "recipes.html"

    recipes_list = [x for x in Recipe.objects.all()]
    cookbook = list(map(lambda x: x.cookbook.name, recipes_list))
    title = list(map(lambda x: x.title, recipes_list))
    recipe = list(map(lambda x: x.recipe, recipes_list))



    return render(request, recipes, {
        "cookbook": cookbook,
        "title": title,
        "recipe": recipe})


def distributors(request):
    distributors = "distributors.html"

    book_distributors = [x for x in BookDistributor.objects.all()]
    dist_list = list(map(lambda x: x.name, book_distributors))
    earnings = list(map(lambda x: x.earnings, book_distributors))


    return render(request, distributors, {
        "distributors": dist_list,
        "earnings": earnings,})


def books(request):
    books = "books.html"

    cookbooks = [x for x in CookBook.objects.all()]
    book_list = list(map(lambda x: x.name, cookbooks))

    return render(request, books, {"books": book_list})