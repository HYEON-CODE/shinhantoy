from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    ord_no = serializers.SerializerMethodField()
    ord_ymd = serializers.DateTimeField(
        read_only=True, format='%Y-%m-%d %H:%M:%S'
    )

    class Meta:
        model = Order
        fields = ('id','ord_no','ord_ymd')
        extra_kwargs = {
            # 값을 가져올 때만 필요
            'id': {
                'read_only': True,
            }
        }