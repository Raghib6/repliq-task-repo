from rest_framework import serializers
from tracker_app import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ["name", "created_at"]
        read_only_fields = ["created_at"]
