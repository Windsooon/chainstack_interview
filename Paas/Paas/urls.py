from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from resources import views

router = routers.DefaultRouter()
router.register(r'resource', views.ResourceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='API Docs')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
