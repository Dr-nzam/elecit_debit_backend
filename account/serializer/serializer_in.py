from rest_framework import serializers
from account.models import CustomUser
from django.utils.text import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = self.Meta.model.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


