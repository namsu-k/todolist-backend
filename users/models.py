from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")

    def total(self):
        return self.todos.all().count()

    def total_done(self):
        return self.todos.filter(done=True).count()

    # def done_rate(self):
    #     rating = round((User.total_done(self) / User.total(self)) * 100, 2)
    #     return f"{rating}%"
