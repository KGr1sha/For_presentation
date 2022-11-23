from django.views.generic import ListView
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Book, Student, Journal
from .serializers import BookSerializer, StudentSerializer, JournalSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def get_queryset(self):
    return Response(Student.objects.filter(class_number=self.kwargs['id']))


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
