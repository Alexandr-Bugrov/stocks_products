from rest_framework import request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer, StockPositionSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['title']
    search_fields = ['description']



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockPositionSerializer
    def get_queryset(self):
        product_name = self.request.query_params.get('products')
        if product_name:
            product = Product.objects.get(title=product_name)
            queryset = Stock.objects.filter(products=product.id)
            return queryset
        else:
            return super().get_queryset()

    def get_serializer_class(self):
        product_name = self.request.query_params.get('products')
        if product_name:
            return StockSerializer








