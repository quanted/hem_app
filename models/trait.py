from django.db import models


class Trait(models.Model):
    """ Trait Category Model """
    title = models.TextField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
