from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Agentprofile

class AgentprofileInline(admin.StackedInline):
    model = Agentprofile
    can_delete = False
    verbose_name_plural = "Agent Profile"


class UserAdmin(BaseUserAdmin):
    inlines = [AgentprofileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)