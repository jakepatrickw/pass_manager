import logging
from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, \
                                    DestroyAPIView, UpdateAPIView

from rest_framework.permissions import AllowAny
from .models import UsernamePasswordService
from .serializer import PassWordSerializer



class ListPassword(ListAPIView):
    queryset = UsernamePasswordService.objects.all()
    serializer_class = PassWordSerializer
    permission_classes = [AllowAny]


class CreatePassword(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PassWordSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeletePassword(DestroyAPIView):
    queryset = UsernamePasswordService.objects.all()
    permission_classes = [AllowAny]
    serializer_class = PassWordSerializer
    lookup_field = 'id'
