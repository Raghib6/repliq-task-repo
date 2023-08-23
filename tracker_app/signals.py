from django.db.models.signals import post_save
from django.dispatch import receiver
from tracker_app.models import Device, DeviceLog, Employee, AssignDevice


@receiver(post_save, sender=AssignDevice)
def update_assign_status(sender, instance, **kwargs):
    instance.device.is_assigned = True
    instance.device.save()
