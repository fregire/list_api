from typing import List
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView

from .models import ListItem
from .serializers import ListItemSerializer


def is_unique(item):
    if not item.parent:
        return True
    for children in item.parent.get_children():
        if children.name == item.name:
            return False
    
    return True
    
class ItemsView(GenericAPIView):
    serializer_class = ListItemSerializer

    def get(self, request):
        list_items = ListItem.objects.all()
        serializer = ListItemSerializer(list_items, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        item = ListItemSerializer(data=request.data)
        if not is_unique(item):
            return Response(data='Имя не уникально в рамках этой ветки')
            
        if item.is_valid():
            item.save()
        else:
            return Response(data=item.errors)

        return Response(status=201)

    

class ItemView(APIView):
    def get(self, request, pk):
        try:
            item = ListItem.objects.get(pk=pk)
        except ListItem.DoesNotExist:
            return Response(status=404)
        serializer = ListItemSerializer(item)

        return Response(serializer.data)
    
    def delete(self, request, pk):
        try:
            item = ListItem.objects.get(pk=pk)
        except ListItem.DoesNotExist:
            return Response(status=404)
        
        item.delete()
        ListItem.objects.rebuild()
        
        return Response(status=201)
    
    def put(self, request, pk):
        item = ListItemSerializer(data=request.data)

        if item.is_valid():
            item.save()
        else:
            return Response(data=item.errors)
        
        return Response(status=200)