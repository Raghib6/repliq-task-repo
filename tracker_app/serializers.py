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


class AssignDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AssignDevice
        fields = [
            "assign_to",
            "device",
            "checkout_date",
            "return_date",
            "device_condition",
            "device_return_condition",
            "description",
        ]

    def to_representation(self, instance):
        rep = super(AssignDeviceSerializer, self).to_representation(instance)
        rep["assign_to"] = instance.assign_to.name
        rep["device"] = instance.device.name
        return rep


class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DeviceLog
        fields = [
            "assigned_device",
            "condition_when_handed_out",
            "condition_when_returned",
            "checkout_date",
            "return_date",
            "comments",
        ]

    def to_representation(self, instance):
        rep = super(DeviceLogSerializer, self).to_representation(instance)
        rep["assigned_device"] = instance.assigned_device.device.name
        return rep
