from rest_framework import mixins, generics
from .serializers import (
    OrderSerializer,
)
from .models import Order
from .paginations import OrderLargePagination

# Order list 보여주는 기능 
class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = OrderSerializer
    pagination_class = OrderLargePagination 

    def get_queryset(self):
        return Order.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
