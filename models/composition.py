from django.db import models


class Composition(models.Model):
    """ Product Composition Model """
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    chemical = models.ForeignKey('Chemical', on_delete=models.CASCADE)
    formulation_id = models.IntegerField()
    productcomp_id = models.IntegerField()
    weight_fraction = models.DecimalField(decimal_places=12, max_digits=16)
    data_type = models.TextField(max_length= 50)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id
