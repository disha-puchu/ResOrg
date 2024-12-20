from django.db import models
from django.contrib.auth.models import User

class UserPicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pid = models.BigAutoField(primary_key=True)
    picpath = models.ImageField()

    def __str__(self) -> str:
        return self.user.username