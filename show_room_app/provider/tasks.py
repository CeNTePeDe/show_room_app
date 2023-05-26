from celery import shared_task


@shared_task()
def set_price(provider_id):
    pass