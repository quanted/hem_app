from django.db import models


class Behavior(models.Model):
    """ Behavior Person Model """
    dataset_id = models.IntegerField(default=1)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    person_household_index = models.IntegerField()
    person_diary = models.IntegerField()
    diary_category = models.TextField(max_length=50)
    gender = models.TextField(max_length=1)
    age = models.IntegerField()
    day_of_year = models.IntegerField(default=1)
    start_time_hr = models.DecimalField(max_digits=6, decimal_places=2)
    duration_hr = models.DecimalField(max_digits=6, decimal_places=2)
    activity_code = models.IntegerField()
    dur_ht  = models.DecimalField(max_digits=6, decimal_places=2)
    dur_iet  = models.DecimalField(max_digits=6, decimal_places=2)
    dur_oet = models.DecimalField(max_digits=6, decimal_places=2)
    dur_det = models.DecimalField(max_digits=6, decimal_places=2)
    flag = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('person', 'dataset_id')
        verbose_name_plural = 'behave_people'