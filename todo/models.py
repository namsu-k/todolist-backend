from django.utils import timezone
from django.db import models
from common.models import CommonModel


class Todo(CommonModel):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="todos",
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )
    done = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.title

    def time_left(self):
        if self.deadline == None:
            return None
        else:
            if self.deadline < timezone.now():
                return "기간 만료"
            else:
                return self.deadline - timezone.now()
