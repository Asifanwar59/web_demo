# D:\gitRepos\website\djangoBckEnd\webdev\websiteDev\fetchStats\views.py
from django.shortcuts import render
from django.shortcuts import redirect
from .models import stats
from .forms import StatsForm
from django.shortcuts import get_object_or_404



def index(request):
    # Now points to fetchStats/templates/fetchStats/index.html
    return render(request, 'fetchStats/index.html')

def stats_list(request):
    stats_entries = stats.objects.all().order_by('-date')  # Order by date descending
    return render(request, 'fetchStats/stats_list.html', {'stats_entries': stats_entries})  

def stats_detail(request, pk):
    stat_entry = get_object_or_404(stats, pk=pk)
    return render(request, 'fetchStats/stats_detail.html', {'stat_entry': stat_entry})  

def stats_create(request):
    if request.method == 'POST':
        form = StatsForm(request.POST, request.FILES)
        if form.is_valid():
            new_stat = form.save(commit=False)
            new_stat.user = request.user  # Assuming the user is logged in
            new_stat.save()
            return redirect('stats_list')
            #return render(request, 'fetchStats/stats_detail.html', {'stat_entry': new_stat})
    else:
        form = StatsForm()
    return render(request, 'fetchStats/stats_form.html', {'form': form})        

def stats_edit(request, pk):
    stat_entry = get_object_or_404(stats, pk=pk)
    if request.method == 'POST':
        form = StatsForm(request.POST, request.FILES, instance=stat_entry)
        if form.is_valid():
            form.save()
            return render(request, 'fetchStats/stats_detail.html', {'stat_entry': stat_entry})
    else:
        form = StatsForm(instance=stat_entry)
    return render(request, 'fetchStats/stats_form.html', {'form': form})        

def stats_delete(request, pk):
    stat_entry = get_object_or_404(stats, pk=pk)
    if request.method == 'POST':
        stat_entry.delete()
        return render(request, 'fetchStats/stats_list.html', {'stats_entries': stats.objects.all().order_by('-date')})
    return render(request, 'fetchStats/stats_confirm_delete.html', {'stat_entry': stat_entry})      


# def about(request):
#     return render(request, 'fetchStats/about.html')     

# def contact(request):
#     return render(request, 'fetchStats/contact.html')   

# def services(request):
#     return render(request, 'fetchStats/services.html')  
