from django.db import models
from django.contrib.auth.models import User

class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gid = models.BigAutoField(primary_key=True)
    gname = models.CharField(max_length=20)
    gdesc = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.user.username
    
class GroupTopic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    tid = models.BigAutoField(primary_key=True)
    tname = models.CharField(max_length=20)
    tdesc = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.user.username