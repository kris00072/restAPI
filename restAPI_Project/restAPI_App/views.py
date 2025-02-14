from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Students
from .serializer import StudentsSerializer
from rest_framework import status

@api_view(['GET'])
def get_data(request):
    data1=Students.objects.all()
    data1=StudentsSerializer(data1, many=True)
    return Response(data1.data) 

@api_view(['POST'])
def create_student(request):
    data=StudentsSerializer(data=request.data)
    if(data.is_valid()):
        data.save()
        return Response(data.data, status=status.HTTP_201_CREATED)
    return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_student(request, pk):
    try:
        data1=Students.objects.get(id=pk)
        data1=StudentsSerializer(data1)
        return Response(data1.data)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_student(request, pk):
    try:
        data1=Students.objects.get(id=pk)
        data=StudentsSerializer(data1, data=request.data)
        if(data.is_valid()):
            data.save()
            return Response(data.data)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        data1=Students.objects.get(id=pk)
        data1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

