from rest_framework import serializers
from . models import UsernamePasswordService


class PassWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsernamePasswordService
        fields = ['service', 'user_name', 'pass_word']