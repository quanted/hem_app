from django.db import models
from hem_app.models.category import Category


class RunHistory(models.Model):
    products = models.BooleanField(default=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    gender = models.CharField(max_length=1, default="B")
    population_size = models.PositiveIntegerField(default=10000)
    min_age = models.PositiveSmallIntegerField(default=0)
    max_age = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('created_at',)
