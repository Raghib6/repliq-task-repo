from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from tracker_app import models
from tracker_app import serializers as model_serializers
from rest_framework.exceptions import ValidationError
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Company"], description="Endpoints to manage Company")
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = model_serializers.CompanySerializer


@extend_schema(tags=["Employee"], description="Endpoints to manage Employee")
class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = model_serializers.EmpolyeeSerializer

    def get_queryset(self):
        company_id = self.kwargs.get("company_id")
        employees = models.Employee.objects.filter(company=company_id)
        return employees


@extend_schema(tags=["Employee"], description="Endpoints to manage Employee")
class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = model_serializers.EmpolyeeSerializer

    def get_object(self):
        company_id = self.kwargs.get("company_id")
        emp_id = self.kwargs.get("emp_id")
        employee = get_object_or_404(models.Employee, company=company_id, id=emp_id)
        return employee


@extend_schema(tags=["Device"], description="Endpoints to manage Device")
class DeviceListCreateView(generics.ListCreateAPIView):
    serializer_class = model_serializers.DeviceSerializer

    def get_queryset(self):
        company_id = self.kwargs.get("company_id")
        devices = models.Device.objects.filter(company=company_id)
        return devices


@extend_schema(tags=["Device"], description="Endpoints to manage Device")
class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = model_serializers.DeviceSerializer

    def get_object(self):
        company_id = self.kwargs.get("company_id")
        device_id = self.kwargs.get("device_id")
        device = get_object_or_404(models.Device, company=company_id, id=device_id)
        return device


@extend_schema(tags=["AssignDevice"], description="Endpoints to manage Assigned Device")
class AssignedDeviceListCreateView(generics.ListCreateAPIView):
    serializer_class = model_serializers.AssignDeviceSerializer

    def get_queryset(self):
        company_id = self.kwargs.get("company_id")
        assigned_devices = models.AssignDevice.objects.filter(
            assign_to__company=company_id
        )
        return assigned_devices

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        device_id = request.data.get("device")
        device = get_object_or_404(models.Device, id=device_id)
        if device.is_assigned:
            raise ValidationError("Device is already taken")
        with transaction.atomic():
            response = super().create(request, *args, **kwargs)
            device.is_assigned = True
            device.save()
        return response


@extend_schema(tags=["AssignDevice"], description="Endpoints to manage Assigned Device")
class AssignedDeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = model_serializers.AssignDeviceSerializer

    def get_object(self):
        company_id = self.kwargs.get("company_id")
        device_id = self.kwargs.get("device_id")
        asigned_device = get_object_or_404(
            models.AssignDevice, assign_to__company=company_id, id=device_id
        )
        return asigned_device


@extend_schema(tags=["DeviceLog"], description="Endpoints to manage Device Logs")
class DeviceLogListView(generics.ListCreateAPIView):
    serializer_class = model_serializers.DeviceLogSerializer

    def get_queryset(self):
        device_logs = []
        company_id = self.kwargs.get("company_id")
        company = models.Company.objects.get(id=company_id)
        devices = company.company_devices.all()
        for device in devices:
            for log in device.assigndevice_set.all():
                device_logs.extend(log.device_logs.all())
        return device_logs
