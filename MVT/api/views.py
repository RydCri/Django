from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getData(request):
    context = {'api_data': 'data from the api'}
    return Response(context)
