from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=100)
    customer_ID = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)   
    start_date = models.DateTimeField(default=datetime.now)       #(auto_now_add=True) #default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    date = models.DateField(default=datetime.now)
    invoice_price = models.IntegerField(default=0)
    reward_points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.agent_name[:11]}"
