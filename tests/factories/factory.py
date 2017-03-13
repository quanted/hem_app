from hem_app.models import Product
import factory

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

        puc_id = factory.Faker('puc_id')
        category_id = factory.Faker('category_id')
        product_type = factory.Faker('product_type')