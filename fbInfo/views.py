from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from fbInfo.models import UserFb
from fbInfo.serializers import UserFbSerializer


class UserFbViewSet(viewsets.ModelViewSet):
    queryset = UserFb.objects.all().order_by('-fb_id')
    serializer_class = UserFbSerializer
    lookup_field = 'fb_id'


class UserFbListView(APIView):
    serializer_class = UserFbSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(UserFb.objects.all(), many=True)
        return Response(serializer.data)


class UserFbDetail(APIView):

    def get_object(self, pk):
        try:
            return UserFb.objects.get(pk=pk)
        except UserFb.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userfb = self.get_object(pk=pk)
        serializer = UserFbSerializer(userfb)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userfb = self.get_object(pk=pk)
        serializer = UserFbSerializer(userfb, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userfb = self.get_object(pk)
        userfb.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
