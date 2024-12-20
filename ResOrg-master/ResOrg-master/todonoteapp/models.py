from django.db import models
from django.contrib.auth.models import User

class UserNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=4000)

    def __str__(self) -> str:
        return self.user.username

class UserTodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tdid = models.BigAutoField(primary_key=True)
    todo = models.CharField(max_length=200)
    tick = models.BooleanField()

    def __str__(self) -> str:
        return self.user.username

