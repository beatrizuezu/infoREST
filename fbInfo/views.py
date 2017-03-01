from rest_framework import viewsets
from fbInfo.models import UserFb
from fbInfo.serializers import UserFbSerializer


class UserFbViewSet(viewsets.ModelViewSet):
    queryset = UserFb.objects.all().order_by('-fb_id')
    serializer_class = UserFbSerializer
