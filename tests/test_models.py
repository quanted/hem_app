import factory
# from factories import ProductFactory, ProductAssignmentFactory, CategoryFactory, RunHistoryFactory, RunParamsFactory
from hem_app.models import Product, Category, ProductAssignment, RunHistory, RunParams
from django.test import TestCase


class ProductFactory(factory.Factory):
    """ Products Factory """
    class Meta:
        model = Product

    category_id = 1
    puc_id = "1234566Y"
    product_type = "Luggage"
    product_type_refined = "Handbag"
    description = "Leather, Gucci"


class CategoryFactory(factory.Factory):
    """ Categories Factory """
    class Meta:
        model = Category

    title = "Baggage"
    description = "Stuff used to carry other stuff around"


class ProductAssignmentFactory(factory.Factory):
    """ Product Assignments Factory """
    class Meta:
        model = ProductAssignment

    short_title = "Some title"
    title = "A longer title"


class RunHistoryFactory(factory.Factory):
    """ Run History Factory """
    class Meta:
        model = RunHistory

    products = True
    gender = "F"
    population_size = 140000
    min_age = 3
    max_age = 99
    categories_id = 1


class RunParamsFactory(factory.Factory):
    """ Run Params Factory """
    class Meta:
        model = RunParams

    ethnicity = "O"
    gender = "B"
    min_age = 4
    max_age = 97
    pop_gen_seed = 97876
    population_size = 180000
    race = "O"


class ProductTestCase(TestCase):
    """ Unit tests for Products """
    def test_string_representation(self):
        product = ProductFactory()
        self.assertEquals(str(product), product.product_type)


class CategoryTestCase(TestCase):
    """ Unit tests for Categories """
    def test_string_representation(self):
        category = CategoryFactory()
        self.assertEquals(str(category), category.title)

    def test_get_top_level(self):
        category = CategoryFactory()
        self.assertEquals(category.get_top_level, NULL)


class ProductAssignmentTestCase(TestCase):
    """ Unit tests for Product Assignments """
    def test_string_representation(self):
        productassignment = ProductAssignmentFactory()
        x = productassignment.short_title + ', ' + productassignment.title
        self.assertEquals(str(productassignment), x)


class RunHistoryTestCase(TestCase):
    """ Unit texts for Run History """
    def test_string_representation(self):
        runhistory = RunHistoryFactory()
        self.assertEquals(str(runhistory), str(runhistory.id))


class RunParamsTestCase(TestCase):
    """ Unit tests for Run Params """
    def test_string_representation(self):
        runparams = RunParamsFactory()
        self.assertEquals(str(runparams), str(runparams.population_size))
