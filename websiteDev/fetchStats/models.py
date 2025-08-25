from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)   
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    value = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text} -  {self.date} - {self.value}"
