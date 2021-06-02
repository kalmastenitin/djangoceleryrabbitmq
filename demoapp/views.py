from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from demoapp.models import *
import json
from demoapp.task import itemqueue

@method_decorator(csrf_exempt,name='dispatch')
class IndexView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            Items.objects.get(item=data.get('item'))
            return JsonResponse({"data":"item already present - add another item"}, status=400)
        except Items.DoesNotExist:
            Items(item=data.get('item')).save()
            itemqueue.delay(data)
            return JsonResponse({"data":"success"}, status=202)
        except Exception as e:
            return JsonResponse({"data":"internal server error"}, status=500)
