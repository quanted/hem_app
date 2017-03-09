from django.db import models


class ProductAssignment(models.Model):
    short_title = models.TextField(max_length=2)
    title = models.TextField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.short_title + ', ' + self.title

    class Meta:
        ordering = ('title',)