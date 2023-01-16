from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound, NotAuthenticated, PermissionDenied
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from .models import Todo
from .serializers import TodoSerializer, TodoDetailSerailzer


class Todolist(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_todo = Todo.objects.all()
        serilaizer = TodoSerializer(
            all_todo,
            many=True,
            context={"request": request},
        )
        return Response(serilaizer.data)

    def post(self, request):
        serializer = TodoDetailSerailzer(
            data=request.data,
            context={"request": request},
        )
        if serializer.is_valid():
            with transaction.atomic():
                todo = serializer.save(
                    user=request.user,
                )
                serializer = TodoDetailSerailzer(
                    todo,
                    context={"request": request},
                )
                return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Todoitem(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoDetailSerailzer(
            todo,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk)
        if todo.user != request.user:
            raise PermissionDenied
        serializer = TodoDetailSerailzer(
            todo,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        if serializer.is_valid():
            updated_todo = serializer.save()
            return Response(
                TodoDetailSerailzer(
                    updated_todo,
                    context={"request": request},
                ).data
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        if todo.user != request.user:
            raise PermissionDenied
        todo.delete()
        return Response(status=HTTP_204_NO_CONTENT)
