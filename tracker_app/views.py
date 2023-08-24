from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from tracker_app import models
from tracker_app import serializers as model_serializers


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = model_serializers.CompanySerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = model_serializers.EmpolyeeSerializer

    def get_queryset(self):
        company_id = self.kwargs.get("company_id")
        employees = models.Employee.objects.filter(company=company_id)
        return employees


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = model_serializers.EmpolyeeSerializer

    def get_object(self):
        company_id = self.kwargs.get("company_id")
        emp_id = self.kwargs.get("emp_id")
        employee = get_object_or_404(models.Employee, company=company_id, id=emp_id)
        return employee


class DeviceListCreateView(generics.ListCreateAPIView):
    serializer_class = model_serializers.DeviceSerializer

    def get_queryset(self):
        company_id = self.kwargs.get("company_id")
        devices = models.Device.objects.filter(company=company_id)
        return devices


class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = model_serializers.DeviceSerializer

    def get_object(self):
        company_id = self.kwargs.get("company_id")
        device_id = self.kwargs.get("device_id")
        device = get_object_or_404(models.Device, company=company_id, id=device_id)
        return device


class AssignedDeviceListCreateView(generics.ListCreateAPIView):
    serializer_class = model_serializers.AssignDeviceSerializer

    def get_queryset(self):
        company_id = self.kwargs.get("company_id")
        assigned_devices = models.AssignDevice.objects.filter(
            assign_to__company=company_id
        )
        return assigned_devices


class AssignedDeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = model_serializers.AssignDeviceSerializer

    def get_object(self):
        company_id = self.kwargs.get("company_id")
        device_id = self.kwargs.get("device_id")
        asigned_device = get_object_or_404(
            models.AssignDevice, assign_to__company=company_id, id=device_id
        )
        return asigned_device
