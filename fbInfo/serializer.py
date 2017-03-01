from rest_framework import serializers
from .models import UserFb


class UserFbSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFb
        fields = ['username', 'name', 'fb_id', 'gender']
