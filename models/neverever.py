from django.db import models


class Neverever(models.Model):
    """ Product Category Model """
    puc_id = models.TextField(max_length=120, default='')
    no2017 = models.BooleanField(default=False)
    hup = models.BooleanField(default=False)
    iup = models.BooleanField(default=False)
    seasonality = models.BooleanField(default=False)
    m = models.BooleanField(default=False)
    f = models.BooleanField(default=False)
    w = models.BooleanField(default=False)
    b = models.BooleanField(default=False)
    a = models.BooleanField(default=False)
    n = models.BooleanField(default=False)
    p = models.BooleanField(default=False)
    o = models.BooleanField(default=False)
    age0_5 = models.BooleanField(default=False)
    age6_12 = models.BooleanField(default=False)
    age13_15 = models.BooleanField(default=False)
    age16_18 = models.BooleanField(default=False)
    age50plus = models.BooleanField(default=False)
    kownrent = models.BooleanField(default=False)
    sewdis = models.BooleanField(default=False)
    dishwash = models.BooleanField(default=False)
    stoven = models.BooleanField(default=False)
    cars = models.BooleanField(default=False)
    pcprint = models.BooleanField(default=False)
    swim = models.BooleanField(default=False)
    yard = models.BooleanField(default=False)
    hot_warm = models.BooleanField(default=False)
    cool = models.BooleanField(default=False)
    cold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.puc_id

    class Meta:
        ordering = ('puc_id',)
