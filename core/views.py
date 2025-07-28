from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    """Dashboard principal del sistema médico"""
    return render(request, 'dashboard.html')