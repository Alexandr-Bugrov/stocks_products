from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['title']
    search_fields = ['description']



class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filterset_fields = ['products']
    def list(self, request):
        product_name = request.get('products')
        if product_name:
            product = Product.objects.get(title=product_name)
            stocks = Stock.objects.filter(product=product.id)

            page = self.paginate_queryset(stocks)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(stocks, many=True)
            return Response(serializer.data)

        else:
            return super().list(self, request)






