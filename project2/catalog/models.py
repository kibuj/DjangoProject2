from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title + "-" + str(self.price)

class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    zip_code = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)

    def __str__(self):
        return self.name + "-" + str(self.zip_code)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title + "-" + str(self.order)