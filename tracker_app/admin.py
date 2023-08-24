from django.contrib import admin
from tracker_app import models


@admin.register(models.Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["name", "is_assigned"]


@admin.register(models.AssignDevice)
class AsignDeviceAdmin(admin.ModelAdmin):
    list_display = ["assign_to", "device", "device_condition"]


admin.site.register(models.Employee)
admin.site.register(models.Company)


@admin.register(models.DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = [
        "assigned_device",
        "condition_when_handed_out",
        "condition_when_returned",
        "checkout_date",
        "return_date",
    ]
