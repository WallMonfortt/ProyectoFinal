from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from core.models import CustomUser


class RegisterUserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    serializer_class = CustomUserSerializer
    model = CustomUser