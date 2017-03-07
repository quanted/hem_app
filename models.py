from django.db import models


class RunHistory(models.Model):
    products = models.BooleanField(default=True)
    gender = models.CharField(max_length=1, default="B")
    population_size = models.PositiveIntegerField(default=10000)
    min_age = models.PositiveSmallIntegerField(default=0)
    max_age = models.PositiveSmallIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('created_at',)


class Category(models.Model):
    title = models.TextField(max_length=120)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class ProductAssignment(models.Model):
    short_title = models.TextField(max_length=2)
    title = models.TextField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.short_title + ', ' + self.title

    class Meta:
        ordering = ('title',)


class Product(models.Model):
    sheds_id = models.TextField(default='', max_length=50)
    sheds_product_category_id = models.TextField(default='', max_length=50)
    puc_id = models.TextField(editable=False)
    group = models.TextField(max_length=75, default='other')
    product_type = models.TextField(max_length=75)
    product_type_refined = models.TextField(max_length=50)
    description = models.TextField()
    assignment = models.ForeignKey(ProductAssignment, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.product_type

    class Meta:
        ordering = ('product_type', 'product_type_refined',)


class RunParams(models.Model):
    ethnicity = models.CharField(max_length=20, default="NMO")
    gender = models.CharField(max_length=1, default="B")
    min_age = models.PositiveSmallIntegerField(default=0)
    max_age = models.PositiveSmallIntegerField(default=100)
    pop_gen_seed = models.PositiveIntegerField(default=1)
    population_size = models.PositiveIntegerField(default=10000)
    race = models.CharField(max_length=20, default="WBNAPO")
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.population_size

    class Meta:
        ordering = ('population_size',)
