from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title + self.price
