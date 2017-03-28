from django.db import models


class Person(models.Model):
    """ Person Category Model """
    run_id = models.IntegerField()
    day = models.IntegerField()
    activity = models.TextField(max_length=200)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)