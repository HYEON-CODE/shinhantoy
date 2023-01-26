from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Too short password')
        # 유효성 검사가 끝난 값을 반환
        return make_password(value)


    class Meta:
        model = Member
        fields = ('id','username','tel','password')
        extra_kwargs = {
            # 값을 가져올 때만 필요
            'id': {
                'read_only': True,
            },
            # 쓸 때만 필요하고 값을 가져올 때는 필요 x
            'password': {
                'write_only': True,
            },
        }