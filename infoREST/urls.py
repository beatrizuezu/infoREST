from django.conf.urls import url, include
from rest_framework import routers
from fbInfo import views

router = routers.DefaultRouter()
router.register(r'UserFb', views.UserFbViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('fbInfo.urls', namespace='rest_framework'))
]
