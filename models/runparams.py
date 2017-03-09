from django.db import models


class RunParams(models.Model):
    ethnicity = models.CharField(max_length=20, default="NMO")
    gender = models.CharField(max_length=1, default="B")
    min_age = models.PositiveSmallIntegerField(default=0)
    max_age = models.PositiveSmallIntegerField(default=100)
    pop_gen_seed = models.PositiveIntegerField(default=1)
    population_size = models.PositiveIntegerField(default=10000)
    race = models.CharField(max_length=20, default="WBNAPO")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.population_size

    class Meta:
        ordering = ('population_size',)