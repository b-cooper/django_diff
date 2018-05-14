
import json
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from difference.models import DiffRequest
from difference.helpers import calculateDifference

def difference(request):
  number = int(request.GET.get('number'))
  print(number)
  try:
    obj = DiffRequest.objects.get(number=number)
    obj.save()
    return HttpResponse(json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), content_type='application/json')
  except DiffRequest.DoesNotExist:
    obj = DiffRequest(number=number, value=calculateDifference(number))
    obj.save()
    return HttpResponse(json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), content_type='application/json')

def differences(request):
  return JsonResponse(list(DiffRequest.objects.all().values('number', 'value', 'datetime', 'last_datetime', 'occurrences')), safe=False)

