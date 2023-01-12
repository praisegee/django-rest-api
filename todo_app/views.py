from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all()

    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def get_task(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({'response': 'Not found'})

    serializer = TaskSerializer(task)
    return Response(serializer.data, 200)


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'response': 'Your task has created!'}, 201)

    return Response(serializer.errors, 400)


@api_view(['PUT', 'GET'])
def update_task(request, id):
    try:
        task = Task.objects.get(pk=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 200)
    except Task.DoesNotExist:
        return Response({'response': 'Not found'})

    serializer = TaskSerializer(task)
    return Response(serializer.data, 200)


@api_view(['GET'])
def delete_task(request, id):
    try:
        task = Task.objects.get(pk=id)
        task.delete()
        return Response({'response': 'Task deleted!'}, 200)
    except Task.DoesNotExist:
        return Response({'response': 'Not found'}, 404)


