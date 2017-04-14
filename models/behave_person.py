from django.db import models


class Behave_Person(models.Model):
    """ Behavior Person Model """
    dataset_id = models.IntegerField(default=1)
    duration = models.DecimalField(max_digits=12, decimal_places=4, default=1)
    formulation_id = models.IntegerField(default=1)
    frequency = models.DecimalField(max_digits=12, decimal_places=4, default=1)
    mass = models.DecimalField(max_digits=12, decimal_places=4, default=1)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    puc_id = models.TextField(max_length=120, default='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('person', 'dataset_id')
        verbose_name_plural = 'behave_people'