import logging
from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, \
                                    DestroyAPIView, UpdateAPIView

from rest_framework.permissions import AllowAny
from .models import UsernamePasswordService
from .serializer import PassWordSerializer, UpdatePassWordSerializer



class ListPassword(ListAPIView):
    queryset = UsernamePasswordService.objects.all()
    serializer_class = PassWordSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]


class CreatePassword(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PassWordSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DeletePassword(DestroyAPIView):
    permission_classes = [AllowAny]
    serializer_class = PassWordSerializer
    queryset = UsernamePasswordService.objects.all()
    lookup_field = 'id'

class UpdatePassword(UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UpdatePassWordSerializer
    queryset = UsernamePasswordService.objects.all()
    lookup_field = 'id'
