from rest_framework import serializers
from tracker_app import models


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ["name", "created_at"]
        read_only_fields = ["created_at"]


class EmpolyeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = ["name", "company"]

    def to_representation(self, instance):
        rep = super(EmpolyeeSerializer, self).to_representation(instance)
        rep["company"] = instance.company.name
        return rep


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = ["name", "company", "is_assigned"]

    def to_representation(self, instance):
        rep = super(DeviceSerializer, self).to_representation(instance)
        rep["company"] = instance.company.name
        return rep
