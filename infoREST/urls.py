from django.conf.urls import url, include
from rest_framework import routers
from fbInfo import views, urls

router = routers.DefaultRouter()
router.register(r'UserFb', views.UserFbViewSet)

urlpatterns = [
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
