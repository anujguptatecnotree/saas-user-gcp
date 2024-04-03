from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class userAccounts(models.Model):
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    contact = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    company= models.TextField(max_length=30)
    account_id = models.CharField(max_length=50, null = True)
    precurement_id = models.CharField(max_length=50, null = True)
