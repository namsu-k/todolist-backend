from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Todo
from .serializers import TodoSerializer, TodoDetailSerailzer


class Todolist(APIView):
    def get(self, request):
        all_todo = Todo.objects.all()
        serilaizer = TodoSerializer(
            all_todo,
            many=True,
        )
        return Response(serilaizer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo = serializer.save()
            return Response(TodoSerializer(todo).data)
        else:
            return Response(serializer.errors)


class Todoitem(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoDetailSerailzer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoDetailSerailzer(
            todo,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_todo = serializer.save()
            return Response(TodoDetailSerailzer(updated_todo).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(HTTP_204_NO_CONTENT)
