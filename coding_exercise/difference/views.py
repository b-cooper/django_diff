from django.shortcuts import render
from django.http import HttpResponse
from difference.models import DiffRequest
from difference.helpers import calculateDifference

def difference(request):
  number = int(request.GET.get('number'))
  print(number)
  try:
    obj = DiffRequest.objects.get(number=number)
    print('ONE EXISTED')
    obj.save()
    return HttpResponse(obj)
  except DiffRequest.DoesNotExist:
    value = calculateDifference(number)
    print('one did not exist')
    obj = DiffRequest(number=number, value=number)
    obj.save()
    return HttpResponse(obj)
  # obj.save() if obj else created.save()
  # print(DiffRequest.objects.all())
