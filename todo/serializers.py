from rest_framework import serializers
from .models import Todo
from users.serializers import TinyUserSerializer


class TodoSerializer(serializers.ModelSerializer):

    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = (
            "pk",
            "title",
            "done",
            "is_owner",
        )

    def get_is_owner(self, todo):
        request = self.context["request"]
        return todo.user == request.user


class TodoDetailSerailzer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    time_left = serializers.SerializerMethodField()
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = "__all__"

    def get_time_left(self, todo):
        return todo.time_left()

    def get_is_owner(self, todo):
        request = self.context["request"]
        return todo.user == request.user
