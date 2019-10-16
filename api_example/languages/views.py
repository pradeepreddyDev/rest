from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializers


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers
