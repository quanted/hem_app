from django.db import models


class Chemical(models.Model):
    """ Product Dose Model """
    dtxrid = models.TextField(max_length=50)
    title = models.TextField(max_length=255)
    cas = models.TextField(max_length=75)
    mw = models.DecimalField(decimal_places=4, max_digits=11)
    vp_pa = models.DecimalField(decimal_places=10, max_digits=16)
    log_kow = models.DecimalField(decimal_places=4, max_digits=11)
    water_sol_mg_L = models.DecimalField(decimal_places=6, max_digits=16)
    log_koa = models.DecimalField(decimal_places=4, max_digits=11)
    hlc_pa_m3_mole = models.DecimalField(decimal_places=10, max_digits=16)
    half_hy_hrs = models.IntegerField()
    half_sediment_hr = models.IntegerField()
    half_soil_hr = models.IntegerField()
    half_water_hr = models.IntegerField()
    half_air_hr = models.DecimalField(decimal_places=10, max_digits=16)
    removal = models.DecimalField(decimal_places=4, max_digits=11)
    kp = models.DecimalField(decimal_places=4, max_digits=11)

    def __str__(self):
        return self.dtxrid + ', ' + self.title

    class Meta:
        ordering = ('title', 'dtxrid',)
