from django.db import models


class RunHistory(models.Model):
    products = models.BooleanField(default=True)
    gender = models.CharField(max_length=1, default="B")
    population_size = models.PositiveIntegerField(default=10000)
    min_age = models.PositiveSmallIntegerField(default=0)
    max_age = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id


class Category(models.Model):
    title = models.TextField(max_length=120)
    description = models.TextField
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title


class Product(models.Model):
    puc_id = models.TextField(editable=False)
    product_type = models.TextField(max_length=75)
    product_type_refined = models.TextField(max_length=50)
    description = models.TextField()
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.product_type