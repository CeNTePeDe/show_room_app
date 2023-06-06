from django.db.models.signals import post_save
from django.dispatch import receiver
from customer.models import Customer


@receiver(post_save, sender=Customer)
def invoke_celery_task_for_customer(sender, instance, **kwargs):
    from customer.tasks import buy_car_from_car_showroom

    buy_car_from_car_showroom.delay(instance.user.id)
