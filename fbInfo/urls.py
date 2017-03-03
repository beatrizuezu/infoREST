from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from fbInfo import views

urlpatterns = [
    url(r'^user_fb/$', views.UserFbListView.as_view()),
    url(r'^user_fb/(?P<pk>[0-9]+)/$', views.UserFbDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
