from rest_framework import serializers
from .models import UserFb
from services import obter_dados_userFb


class UserFbSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserFb
        fields = ('fb_id', 'username', 'name', 'gender')
        read_only_fields = ('username', 'name', 'gender')

    def validate_fb_id(self, fb_id):
        try:
            self.dados = obter_dados_userFb(fb_id)
        except:
            raise serializers.Validationerror('Facebook user doesn\'t exists')

    def create(self, instance):
        return UserFb.objects.create(**self.dados)

    def read(self, instance):
        return self.list(instance)
