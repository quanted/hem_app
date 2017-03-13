from factories import *
from django.test import TestCase


class ProductTestCase(TestCase):


    def test_string_representation(self):
        product = ProductFactory()
        self.assertEquals(str(product), product.product_type)


class CategoryTestCase(TestCase):

    def test_string_representation(self):
        category = CategoryFactory()
        self.assertEquals(str(category), category.title)


class ProductAssignmentTestCase(TestCase):

    def test_string_representation(self):
        productassignment = ProductAssignmentFactory()
        x = productassignment.short_title + ', ' + productassignment.title
        self.assertEquals(str(productassignment), x)


class RunHistoryTestCase(TestCase):

    def test_string_representation(self):
        runhistory = RunHistoryFactory()
        self.assertEquals(str(runhistory), str(runhistory.id))


class RunParamsTestCase(TestCase):

    def test_string_representation(self):
        runparams = RunParamsFactory()
        self.assertEquals(str(runparams), str(runparams.population_size))
