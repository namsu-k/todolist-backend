from rest_framework import serializers
from .models import Todo
from users.serializers import TinyUserSerializer


class TodoSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = Todo
        fields = (
            "pk",
            "title",
            "description",
            "deadline",
            "done",
            "user",
        )


class TodoDetailSerailzer(serializers.ModelSerializer):

    user = TinyUserSerializer()

    class Meta:
        model = Todo
        fields = "__all__"
