from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=150)
    company = models.ForeignKey(
        Company, related_name="employees", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=150)
    company = models.ForeignKey(
        Company, related_name="company_devices", on_delete=models.CASCADE
    )
    is_assigned = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class AssignDevice(models.Model):
    CONDITIONS = (
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Fair", "Fair"),
        ("Poor", "Poor"),
        ("Broken", "Broken"),
    )
    assign_to = models.ForeignKey(
        Employee, related_name="employee_devices", on_delete=models.CASCADE
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    device_condition = models.CharField(max_length=15, choices=CONDITIONS)
    device_return_condition = models.CharField(
        null=True, blank=True, max_length=15, choices=CONDITIONS
    )
    description = models.TextField()

    def __str__(self):
        return self.assign_to.name


class DeviceLog(models.Model):
    employee = models.CharField(max_length=250)
    condition_when_handed_out = models.CharField(max_length=15)
    condition_when_returned = models.CharField(max_length=15)
    checkout_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.employee.name
