from statistics import mode
from turtle import ondrag
from django.db import models
from core.models import CustomUser
# Create your models here.
class New(models.Model):
    title = models.CharField(
        max_length=150
    )
    body = models.TextField()
    # image = models.ImageField(
    #     upload_to='news/images/',
    #     blank=True,
    #     null=True
    # )
    auhtor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self) -> str:
        return self.title

class Tags(models.Model):
    name = models.CharField(
        max_length=50
    )
    slug = models.SlugField(
        max_length=50,
        unique=True
    )