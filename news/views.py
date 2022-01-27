from re import T
from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import New, Tags
from .serializers import NewSerializer, TagSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title']
    search_fields = ['=auhtor']
    ordering_fields = ['name', 'id']

    @action(detail=True, methods=["GET"])
    def get_tags(self, request, pk=None):
        comments = Tags.objects.all().filter(
            new_id=pk
        )
        serialized = TagSerializer(comments, many=True)
        return Response(serialized.data)