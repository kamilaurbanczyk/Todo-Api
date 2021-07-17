from django.shortcuts import render
from rest_framework.views import APIView
from .models import TodoItem
from .serializer import TodoSerializer
from rest_framework.response import Response


class TodoList(APIView):
    def get(self, request):
        todos = TodoItem.objects.all()
        todo_data = TodoSerializer(todos, many=True)
        return Response(todo_data.data)

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        if todo.is_valid():
            todo.save()
        return Response(todo.data)

    def delete(self, request):
        TodoItem.objects.all().delete()
        return Response(None)


class TodoOne(APIView):
    pass
