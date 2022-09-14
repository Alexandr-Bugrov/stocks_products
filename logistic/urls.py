from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet
from django.urls import path

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [path('')

              ] + router.urls
