from django.urls import path, include
from .views import BookViewSet, StudentViewSet, JournalViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'book', BookViewSet)
router.register(r'student', StudentViewSet)
router.register(r'journal', JournalViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
