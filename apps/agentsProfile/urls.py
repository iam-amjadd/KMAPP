from django.urls import path, include

from apps.agentsSchedule.views import agentSchedule, update_or_create_agentshift
from .views import agentsList, editAgentProfile, register_user, change_password

urlpatterns = [

    path('', agentsList, name='agentsList'),
    path('reg/', register_user, name='agentregister'),
    path('<str:username>/', include([
        path('', editAgentProfile, name='agentDetail'),
        path('change-password/', change_password, name='change_password'),
        path('edit/', update_or_create_agentshift, name='update_or_create_agentshift'),
        path('schedule/', agentSchedule, name='agentSchedule'),
    ])),
]
