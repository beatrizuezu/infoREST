from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from fbInfo.models import UserFb

class UserFbTests(APITestCase):

    def test_post(self):
        data = {'fb_id': '562073097'}
        request = self.client.post('/userFb/', data, format='json')
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserFb.objects.count(), 1)
        self.assertEqual(UserFb.objects.get().fb_id, '562073097')
