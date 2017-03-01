from django.db import models

class RunHistory(models.Model):
    products = models.BooleanField(default=True)
    gender = models.CharField(max_length=1, default="B")
    population_size = models.PositiveIntegerField(default=10000)
    min_age = models.PositiveSmallIntegerField(default=0)
    max_age = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)