from django.db.models.signals import post_save
from django.dispatch import receiver
from tracker_app.models import AssignDevice, DeviceLog


@receiver(post_save, sender=AssignDevice)
def update_assign_status(sender, instance, **kwargs):
    if not instance.return_date and instance.device_return_condition:
        instance.device.is_assigned = True
    else:
        instance.device.is_assigned = False
    instance.device.save()


@receiver(post_save, sender=AssignDevice)
def update_create_log(sender, instance, created, **kwargs):
    if created:
        rc = instance.device_return_condition or "Not Returned Yet"
        DeviceLog.objects.create(
            assigned_device=instance,
            condition_when_handed_out=instance.device_condition,
            condition_when_returned=rc,
            checkout_date=instance.checkout_date,
            return_date=instance.return_date,
            comments=instance.description,
        )
    else:
        log = DeviceLog.objects.get(assigned_device=instance.id)
        if log:
            log.condition_when_returned = instance.device_return_condition
            log.return_date = instance.return_date
            log.comments = instance.description
            log.save()
