from django.db import models


class Category(models.Model):
    """ Product Category Model """
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title
