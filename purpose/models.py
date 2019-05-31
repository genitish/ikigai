from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Section(models.Model):
    name=models.CharField(max_length=250)

    def __str__(self):
        return self.name

class list(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.TextField()
    section=models.ForeignKey('Section',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)+" by"+str(self.user.username)

