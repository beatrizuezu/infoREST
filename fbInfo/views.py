from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from fbInfo.models import UserFb
from fbInfo.serializers import UserFbSerializer


class UserFbViewSet(viewsets.ModelViewSet):
    queryset = UserFb.objects.all().order_by('-fb_id')
    serializer_class = UserFbSerializer


class UserFbListView(APIView):
    serializer_class = UserFbSerializer


    def get(self, request, format=None):
        serializer = self.serializer_class(UserFb.objects.all(), many=True)
        return Response(serializer.data)
