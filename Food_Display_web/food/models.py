from django.db import models

# Create your models here.
class Item(models.Model):

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=500,default="https://i0.wp.com/servedcatering.com/wp-content/uploads/2021/05/menu-item-placeholder.png?ssl=1")


    def __str__(self):
        return self.item_name