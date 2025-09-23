import graphene
from graphene_django import DjangoObjectType
from products.models import Product, Category

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_categories = graphene.List(CategoryType)

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_all_categories(root, info):
        return Category.objects.all()

schema = graphene.Schema(query=Query)
