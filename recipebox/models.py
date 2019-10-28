"""
Author
    Name

NewsItem
    Date
    Title
    Body
    author
"""
from django.db import models

class CookBook(models.Model):
    bookdistributor = models.ForeignKey("BookDistributor", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    cookbook = models.ForeignKey("CookBook", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    recipe = models.TextField()

    def __str__(self):
        print(f"{self.title} - {self.cookbook.name}")
        return f"{self.title} - {self.cookbook.name}"

class BookDistributor(models.Model):
    name = models.CharField(max_length=50)
    earnings = models.IntegerField()