from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customers
from .serializer import CustomerSerializer

class CustomerList(APIView):    
    def get(self, request):
        data1=Customers.objects.all()
        data1=CustomerSerializer(data1, many=True)
        return Response(data1.data)
    
    def post(self, request):
        data=CustomerSerializer(data=request.data)
        if(data.is_valid()):
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomerDetail(APIView):
    def get(self, request, pk):
        try:
            data1=Customers.objects.get(id=pk)
            data1=CustomerSerializer(data1)
            return Response(data1.data)
        except Customers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        try:
            data1=Customers.objects.get(id=pk)
            data=CustomerSerializer(data1, data=request.data)
            if(data.is_valid()):
                data.save()
                return Response(data.data)
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Customers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            data1=Customers.objects.get(id=pk)
            data1.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Customers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

