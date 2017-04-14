from django.db import models


class Behave_Activity(models.Model):
    """ Behavior Activity Model """
    title = models.TextField(max_length=120, default='')
    day_of_year = models.IntegerField(default=1)
    dataset_id = models.IntegerField(default=1)
    puc_id = models.TextField(max_length=120, default='')
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    start_time = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('person', 'dataset_id')
        verbose_name_plural = 'behave_activities'