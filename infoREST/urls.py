from django.conf.urls import url, include
from django.contrib import admin
from fbInfo import views

router = routers.DefaultRouter()
router.register(r'UserFb', views.UserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('fbInfo.urls', namespace='rest_framework'))
]
