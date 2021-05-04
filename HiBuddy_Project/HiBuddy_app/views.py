# from django.shortcuts import render

# from rest_framework import viewsets

# class EmployeeViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

@api_view(['GET'])
def index(request):
	api_urls = {
		# 'List':'/task-list/',
		# 'Detail View':'/task-detail/<str:pk>/',
		# 'Create':'/task-create/',
		# 'Update':'/task-update/<str:pk>/',
		# 'Delete':'/task-delete/<str:pk>/',
        # =================================================
        'List':'/show/',
		'Detail View':'/preview/<int:id>/',
		'Create':'/add/',
		'Update':'/update/<int:id>/',
		'Delete':'/delete/<int:id>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def show(request):
	emp = Employee.objects.all()
	serializer = EmployeeSerializer(emp, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def add(request):
	serializer = EmployeeSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['GET'])
def preview(request, id):
	emp = Employee.objects.get(id=id)
	serializer = EmployeeSerializer(emp, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def update(request, id):
	emp = Employee.objects.get(id=id)
	serializer = EmployeeSerializer(instance=emp, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, id):
	emp = Employee.objects.get(id=id)
	emp.delete()
	return Response('Employee succsesfully delete!')
