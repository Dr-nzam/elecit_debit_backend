from django.db import models
from account.models import CustomUser
# Create your models here.

class Debit(models.Model):
    nom_debit = models.CharField(max_length=128, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='debit')
    visible = models.BooleanField(default=True)