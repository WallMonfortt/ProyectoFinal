from pyexpat import model
from rest_framework import serializers
from .models import New, Tags


class TagSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Tags
        fields = ('__all__')


class NewSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model= New
        fields = ('__all__')