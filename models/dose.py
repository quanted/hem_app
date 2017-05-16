from django.db import models


class Dose(models.Model):
    """ Product Dose Model """
    runparams = models.ForeignKey('RunParams', on_delete=models.CASCADE)
    chemical = models.ForeignKey('Chemical', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    day = models.IntegerField()
    intake_ingest_mgkgBW_d = models.DecimalField(decimal_places=15, max_digits=16)
    intake_derm_mgkgBW_d = models.DecimalField(decimal_places=6, max_digits=14)
    intake_inhal_mgkgBW_d = models.DecimalField(decimal_places=6, max_digits=10)
    peak_hourly_air_conc_ug_m3 = models.DecimalField(decimal_places=6, max_digits=14)
    peak_dermal_loading_ug = models.DecimalField(decimal_places=6, max_digits=10)
    disposal_solid_waste_ug = models.DecimalField(decimal_places=6, max_digits=15)
    disposal_window_ug = models.DecimalField(decimal_places=6, max_digits=14)
    disposal_sanitary_drain_ug = models.DecimalField(decimal_places=6, max_digits=16)
    disposal_outdoor_surface_ug = models.DecimalField(decimal_places=6, max_digits=14)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    def __unicode__(self):
        return unicode(self.id) or u''

    class Meta:
        ordering = ('id',)
