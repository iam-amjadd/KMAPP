from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.agentsProfile.models import Agentprofile
from django.shortcuts import get_object_or_404

@login_required(login_url="auth/login")
def index(request):
    return render(request, 'pages/plain_page.html')