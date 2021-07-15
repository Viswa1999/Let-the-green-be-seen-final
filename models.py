from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='product_pictures')
    product_description = models.CharField(max_length=200)
    product_amount = models.FloatField(null=True)




