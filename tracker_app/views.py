from django.shortcuts import render
from rest_framework import generics, viewsets
from tracker_app import models
from tracker_app import serializers as model_serializers


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = model_serializers.CompanySerializer
