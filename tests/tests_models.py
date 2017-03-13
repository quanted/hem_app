import factories
from django.test import TestCase


class ProductTestCase(TestCase):
    """Unit tests for Products"""
    def test_string_representation(self):
        product = factories.ProductFactory()
        self.assertEquals(str(product), product.product_type)


class CategoryTestCase(TestCase):
    """Unit tests for Categories"""
    def test_string_representation(self):
        category = factories.CategoryFactory()
        self.assertEquals(str(category), category.title)


class ProductAssignmentTestCase(TestCase):
    """Unit tests for Product Assignments"""
    def test_string_representation(self):
        productassignment = factories.ProductAssignmentFactory()
        x = productassignment.short_title + ', ' + productassignment.title
        self.assertEquals(str(productassignment), x)


class RunHistoryTestCase(TestCase):
    """Unit texts for Run History"""
    def test_string_representation(self):
        runhistory = factories.RunHistoryFactory()
        self.assertEquals(str(runhistory), str(runhistory.id))


class RunParamsTestCase(TestCase):
    """Unit tests for Run Params"""
    def test_string_representation(self):
        runparams = factories.RunParamsFactory()
        self.assertEquals(str(runparams), str(runparams.population_size))
