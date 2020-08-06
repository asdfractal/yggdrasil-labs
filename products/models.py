from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False, default="")
    booking_required = models.BooleanField(default=False, null=False, blank=False)
    shipping_required = models.BooleanField(default=False, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
