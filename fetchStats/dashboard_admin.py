# In fetchStats/admin.py
from django.contrib import admin
from django.db.models import Sum
from django.urls import path
from django.shortcuts import render
from .models import stats
import json

class MyAdminSite(admin.AdminSite):
    site_header = "My Custom Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('dashboard/', self.admin_view(self.dashboard_view), name='dashboard'),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        # Aggregate data for the pie chart
        stats_data = stats.objects.values('agent_name').annotate(
            total_reward_points=Sum('reward_points')
        )
        
        # Prepare data for the Chart.js
        labels = [item['agent_name'] for item in stats_data]
        data = [item['total_reward_points'] for item in stats_data]
        
        # You can add more colors if you expect more agents
        colors = [
            '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'
        ]
        
        chart_data = {
            'labels': labels,
            'data': data,
            'colors': colors[:len(labels)],
        }

        context = {
            'chart_data': json.dumps(chart_data)
        }
        return render(request, 'admin/dashboard.html', context)

# Instantiate your custom admin site
my_admin_site = MyAdminSite(name='myadmin')

# Register your model with the custom admin site
my_admin_site.register(stats)
