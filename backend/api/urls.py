from django.urls import path, include
from .views import BookViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
