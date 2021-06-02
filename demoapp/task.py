from celery import shared_task
from demoapp.models import *


@shared_task
def itemqueue(item):    
    item = Items.objects.get(item=item['item'])
    print(item)
    item.status="completed"
    item.save()
    return None