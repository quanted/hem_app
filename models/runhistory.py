from django.db import models




GENDER_CHOICES = (
	('B', 'Both'),
	('F', 'Female'),
	('M', 'Male')
)

class RunHistory(models.Model):
    """ Run History Model """
    is_product = models.BooleanField(default=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    chemical = models.ForeignKey('Chemical', on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=1, default="B", choices=GENDER_CHOICES)
    population_size = models.PositiveIntegerField(default=10000)
    min_age = models.PositiveSmallIntegerField(default=0)
    max_age = models.PositiveSmallIntegerField(default=99)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('created_at',)
