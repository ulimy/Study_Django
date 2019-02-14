from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

# ModelSerializer --> 모델을 serializer 해주는 함수
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model에 user을 넣어 읽기만@
        model = User
        fields = ('username', 'email')


class PostSerializer(serializers.ModelSerializer):
    # 사용자가 변경할 수 없도록 read_only
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'subtitle',
            'content',
            'created_at',
        )
        read_only_fields = ('created_at',)
