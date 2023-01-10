from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import Todo
from .serializers import TodoSerializer


class Todolists(APIView):
    def get(self, request):
        all_todo = Todo.objects.all()
        serilaizer = TodoSerializer(
            all_todo,
            many=True,
        )
        return Response(serilaizer.data)

    # def post(self, request):
    #     pass


# class Todoitem(APIView):
#     def get_object(self, pk):
#         try:
#             return Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist:
#             raise NotFound

#     def get(self, request, pk):
#         serializer = TodoSerializer(self.get_object(pk))
#         return Response(serializer.data)

#     def put(self, request, pk):
#         serializer = TodoSerializer(
#             self.get_object(pk),
#             data=request.data,
#             partial=True,
#         )
#         if serializer.is_valid():
#             update_todo = serializer.save()
#             return Response(TodoSerializer(update_todo).data)

#     def delete(self, request, pk):
#         pass
