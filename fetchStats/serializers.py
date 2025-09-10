# <your_api_app>/serializers.py
from rest_framework import serializers
#from stats.models import Task # Import the model from your existing app
from .models import stats 

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = stats # Use the model defined in fetchStats/models.py
        fields = '__all__' # Expose all fields
