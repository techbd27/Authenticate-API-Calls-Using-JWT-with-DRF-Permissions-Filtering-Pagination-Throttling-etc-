from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task, Contact, Author, Book
from .serializers import (
    TaskSerializer,
    ContactSerializer,
    AuthorSerializer,
    BookSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class TaskPagination(PageNumberPagination):
    page_query_param = "lalala"
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    # throttle_classes [
    #     UserRateThrottle,
    # ]

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ["completed"]
    search_fields = ["title", "description"]
    ordering_fields = ["id", "title", "completed", "created_at"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
        # return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(detail=False, methods=["get"])
    def say_hello(self, request):
        return Response({"message": "Hello, World!"})


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
