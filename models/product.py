from django.db import models
from productassignment import ProductAssignment
from category import Category


class Product(models.Model):
    sheds_id = models.TextField(max_length=50, blank=True)
    sheds_product_category_id = models.TextField(max_length=50, blank=True)
    puc_id = models.TextField(blank=True)
    group = models.TextField(max_length=75, default='other')
    product_type = models.TextField(max_length=75)
    product_type_refined = models.TextField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    assignment = models.ForeignKey(ProductAssignment, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.product_type

    class Meta:
        ordering = ('product_type', 'product_type_refined',)
