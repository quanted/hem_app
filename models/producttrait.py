from django.db import models


class ProductTrait(models.Model):
    '''Linking model for Product and Trait'''
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    trait = models.ForeignKey('Trait', on_delete=models.CASCADE)
