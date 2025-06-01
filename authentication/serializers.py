from rest_framework import serializers
from .models import CustomUser
from .managers import CustomUserManager
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        return CustomUserManager.objects.create_user(**validated_data)