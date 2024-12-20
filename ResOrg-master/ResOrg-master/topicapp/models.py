from django.db import models
from django.contrib.auth.models import User
from dashboardapp.models import UserGroup, GroupTopic

class TopicSection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    topic = models.ForeignKey(GroupTopic, on_delete=models.CASCADE)
    sid = models.BigAutoField(primary_key=True)
    sname = models.CharField(max_length=20, unique=True)
    sdesc = models.CharField(max_length=100)

class TopicResource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    topic = models.ForeignKey(GroupTopic, on_delete=models.CASCADE)
    section = models.ForeignKey(TopicSection, on_delete=models.CASCADE)
    rid = models.BigAutoField(primary_key=True)
    rname = models.CharField(max_length=20, unique=True)
    rvalue = models.FileField()
    rtype = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.user.username