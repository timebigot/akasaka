from django.db import models
from django.conf import settings

class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    def __str__(self):
        return self.cat_name

menu_path = settings.STATIC_PATH + '/img/menu'
class Menu(models.Model):
    item_name = models.CharField(max_length=30)
    detail = models.CharField(max_length=100, blank=True)
    image = models.CharField(max_length=50)
    price = models.CharField(max_length=10, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    in_season = models.BooleanField(default=1)
    is_lunch = models.BooleanField(default=0)
    how_spicy = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.item_name
