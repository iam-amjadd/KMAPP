from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import Agentprofile
from .forms import UserRegistrationForm, AgentProfileEditForm

@login_required(login_url="/auth/login")
def agentsList(request):
    agents_list = Agentprofile.objects.exclude(user__is_staff=True)
    context = {'agents_list': agents_list}

    return render(request, 'pages/agents_list.html', context)

@login_required(login_url="/auth/login")
def editAgentProfile(request, username):
    agent = get_object_or_404(Agentprofile, user__username=username)
    if request.method == 'POST':
        form = AgentProfileEditForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            return redirect('agentsList')
    else:
        form = AgentProfileEditForm(instance=agent)

    return render(request, 'pages/agent_detail.html', {'form': form})

@login_required(login_url="/auth/login")
def register_user(request):
    if not request.user.is_staff:
        return render(request, 'errors/page_403.html', status=403)
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agentsList')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'pages/register_user.html', {'form': form})

@login_required(login_url="/auth/login")
def change_password(request , username):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', 'agentDetail'))
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'pages/change_password.html', {'form': form})
