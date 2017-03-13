import factory
from hem_app.models import Product, Category, ProductAssignment, RunHistory, RunParams


class ProductFactory(factory.Factory):
    # Products Factory
    class Meta:
        model = Product

    category_id = 1
    puc_id = "1234566Y"
    product_type = "Luggage"
    product_type_refined = "Handbag"
    description = "Leather, Gucci"


class CategoryFactory(factory.Factory):
    # Categories Factory
    class Meta:
        model = Category

    title = "Baggage"
    description = "Stuff used to carry other stuff around"


class ProductAssignmentFactory(factory.Factory):
    # Product Assignments Factory
    class Meta:
        model = ProductAssignment

    short_title = "Some title"
    title = "A longer title"


class RunHistoryFactory(factory.Factory):
    # Run History Factory
    class Meta:
        model = RunHistory

    products = True
    gender = "F"
    population_size = 140000
    min_age = 3
    max_age = 99
    categories_id = 1


class RunParamsFactory(factory.Factory):
    # Run Params Factory
    class Meta:
        model = RunParams

    ethnicity = "O"
    gender = "B"
    min_age = 4
    max_age = 97
    pop_gen_seed = 97876
    population_size = 180000
    race = "O"

