from django.db import models


class Person(models.Model):
    """ Person Category Model """
    dataset_id = models.IntegerField(default=1)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length=1)
    ethnicity = models.CharField(max_length=1, default='W')
    age_years = models.IntegerField(default=1)
    ages = models.TextField(max_length=30)
    baths = models.IntegerField(default=1)
    bsa_adj = models.DecimalField(max_digits=10, decimal_places=3, default=0)
    cars = models.IntegerField(default=1)
    cwasher = models.IntegerField(default=1)
    dishwash = models.IntegerField(default=1)
    dryer = models.IntegerField(default=1)
    dryruse = models.IntegerField(default=1)
    genders = models.CharField(max_length=30)
    high_ceil = models.IntegerField(default=0)
    kownrent = models.IntegerField(default=1)
    lot = models.IntegerField(default=1)
    outgrill = models.IntegerField(default=1)
    pcprint = models.IntegerField(default=1)
    pool = models.IntegerField(default=1)
    row = models.IntegerField(default=1)
    sewdis = models.IntegerField(default=1)
    state = models.IntegerField(default=1)
    stoven = models.IntegerField(default=1)
    swim = models.IntegerField(default=1)
    unitsf = models.IntegerField(default=1)
    washload = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)
