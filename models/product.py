from django.db import models


class Product(models.Model):
    """ Product model """
    title = models.TextField(max_length=255)
    description = models.TextField(blank=True)
    puc_id = models.TextField(max_length=17, default='')
    sheds_id = models.TextField(max_length=12, default='')
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE, default=1)
    traits = models.ForeignKey('Trait', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
