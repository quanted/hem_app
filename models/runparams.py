from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class RunParams(models.Model):
    """ Model for storing params for each run """
    ethnicity = models.CharField(max_length=20, default="NMO")
    gender = models.CharField(max_length=1, default="B")
    min_age = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(100)])
    max_age = models.PositiveSmallIntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(100)])
    pop_gen_seed = models.PositiveIntegerField(default=1)
    comp_method = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(2)])
    chem_seed = models.PositiveIntegerField(default=1)
    house_seed = models.PositiveIntegerField(default=1)
    puc_seed = models.PositiveIntegerField(default=1)
    puc_offset = models.PositiveIntegerField(default=1)
    population_size = models.PositiveIntegerField(default=10000)
    race = models.CharField(max_length=20, default="WBNAPO")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True)
    notes = models.TextField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.population_size)
