from django.apps import AppConfig

class AppsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps'
    label = 'apps'

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

class AgentsprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agentsProfile'

class AgentsscheduleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'agentsSchedule'