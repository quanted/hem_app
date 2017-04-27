from django.db import models


class Habit(models.Model):
    """  Habit Model """

    product = models.ForeignKey('Person', on_delete=models.CASCADE)
    variable_value = models.TextField(max_length=25, default='')
    units = models.TextField(max_length=25, default='')
    gender = models.CharField(max_length=1)
    min_age = models.IntegerField(default=0)
    max_age = models.IntegerField(default=99)
    form_value = models.TextField(max_length=25, default='')
    mean_value = models.DecimalField(decimal_places=7, max_digits=14)
    cv_value = models.DecimalField(decimal_places=7, max_digits=14)

    def __str__(self):
        return self.puc_id

    class Meta:
        ordering = ('id',)