from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from apps.agentsProfile.models import Agentprofile
from .models import Agentshift
from .forms import AgentshiftForm

def update_or_create_agentshift(request, username):
    agent = get_object_or_404(Agentprofile, user__username=username)
    if request.method == 'POST':
        try:
            agentshift = Agentshift.objects.get(user=agent.user, date=request.POST['date'])
        except Agentshift.DoesNotExist:
            agentshift = None
            #return JsonResponse({'success': False, 'errors': 'Agentshift does not exist.'})

        form = AgentshiftForm(request.POST, instance=agentshift)
        if form.is_valid():
            agentshift = form.save()
            event = {
                'title': agentshift.shifts.name,
                'start': agentshift.date.isoformat(),
                'end': agentshift.date.isoformat(),
                'description': f'{agentshift.shifts.start_time.strftime("%H:%M")} - {agentshift.shifts.end_time.strftime("%H:%M")}',
            }
            return JsonResponse({'success': True, 'event': event})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        return JsonResponse({'success': False})

@login_required(login_url="/auth/login")
def agentSchedule(request, username):
    agent = get_object_or_404(Agentprofile, user__username=username)
    is_owner = request.user == agent.user
    is_admin_profile = agent.user.is_superuser
    is_staff = request.user.is_staff

    if is_owner or is_staff or not is_admin_profile:
        agentshifts = Agentshift.objects.filter(user=agent.user)
        form = AgentshiftForm(instance=agent)  # Create an instance of the AgentshiftForm
        context = {'agent':agent,'agentshifts': agentshifts, 'form': form}
        return render(request, 'pages/shifts_calender.html', context)
    else:
        return render(request, 'errors/page_403.html', status=403)
