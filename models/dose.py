from django.db import models


class Dose(models.Model):
    """ Product Dose Model """
    runparams = models.ForeignKey('RunParams', on_delete=models.CASCADE)
    chemical = models.ForeignKey('Chemical', on_delete=models.CASCADE)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    day = models.IntegerField()
    dir_derm_exp = models.FloatField()
    dir_derm_max = models.FloatField()
    dir_derm_abs = models.FloatField()
    dir_inhal_exp = models.FloatField()
    dir_inhal_mass = models.FloatField()
    dir_inhal_max = models.FloatField()
    dir_inhal_abs = models.FloatField()
    dir_ingest_exp = models.FloatField()
    dir_ingest_abs = models.FloatField()
    release = models.FloatField()
    ind_derm_exp = models.FloatField()
    ind_derm_max = models.FloatField()
    ind_derm_abs = models.FloatField()
    ind_inhal_exp = models.FloatField()
    ind_inhal_max = models.FloatField()
    ind_inhal_mass = models.FloatField()
    ind_inhal_abs = models.FloatField()
    ind_ingest_exp = models.FloatField()
    ind_ingest_abs = models.FloatField()
    out_sur = models.FloatField()
    out_air = models.FloatField()
    drain = models.FloatField()
    waste = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    def __unicode__(self):
        return unicode(self.id) or u''

    class Meta:
        ordering = ('id',)
