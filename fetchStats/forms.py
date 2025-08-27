from django import forms
from .models import stats  

class StatsForm(forms.ModelForm):
    class Meta:
        model = stats
        fields = ['agent_name', 'customer_ID', 'photo', 'start_date', 'end_date', 'date', 'invoice_price', 'reward_points'] # Include all fields except 'user'
