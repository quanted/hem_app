from django.db import models


class LifeCycleImpact(models.Model):
    """  LifeCycleImpact Model """
    runparams = models.ForeignKey('RunParams', on_delete=models.CASCADE)
    chemical = models.ForeignKey('Chemical', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    mass_frac_chem_puc = models.FloatField()
    mass_puc_use_adult = models.FloatField()
    pif_derm_adult = models.FloatField()
    pif_inhal_adult = models.FloatField()
    pif_ingest_adult = models.FloatField()
    mass_puc_use_child = models.FloatField()
    pif_derm_child = models.FloatField()
    pif_inhal_child = models.FloatField()
    pif_ingest_child = models.FloatField()
    chem_mass = models.FloatField()
    mass_tot_air = models.FloatField()
    mass_tot_water = models.FloatField()
    mass_tot_land = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)