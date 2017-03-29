from django.db import models
from .assignment import Assignment
from .category import Category


class Product(models.Model):
    """ Product model """
    title = models.TextField(max_length=255)
    description = models.TextField(blank=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, default=1)
    traits = models.ManyToManyField('Trait', through='ProductTrait')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.product_type

    class Meta:
        ordering = ('title',)
