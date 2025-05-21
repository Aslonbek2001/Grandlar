from django.db import models
from users.models import User


class DepOne(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='depone')

class DepTwo(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='deptow')


class DepFin(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='depfin')

