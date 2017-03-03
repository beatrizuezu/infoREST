from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from fbInfo.models import UserFb
import json

class UserFbTests(APITestCase):

    def test_post(self):
        data = {'fb_id': '562073097'}
        response = self.client.post('/user_fb/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserFb.objects.count(), 1)
        self.assertEqual(UserFb.objects.get().fb_id, '562073097')

    def test_get(self):
        response = self.client.get('/user_fb/')
        self.assertEqual(len(response.json()), UserFb.objects.count())

    def test_delete(self):
        response = self.client.delete('/user_fb/562073097/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
