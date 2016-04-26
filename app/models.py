from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name

class Menu(models.Model):
    item_name = models.CharField(max_length=30)
    detail = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_season = models.BooleanField(default=1)

    def __str__(self):
        return self.item_name
