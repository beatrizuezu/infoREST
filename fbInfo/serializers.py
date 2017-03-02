from rest_framework import serializers
from .models import UserFb
from services import obter_dados_userFb


class UserFbSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFb
        fields = ['fb_id']

    def create(self, fb_id, validated_data):
        dados = obter_dados_userFb(fb_id)
        return dados(**validated_data)
