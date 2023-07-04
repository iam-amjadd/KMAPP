from django.contrib import admin
from django.urls import path, include
from apps.home.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('agents/', include("apps.agentsProfile.urls")), # AgentsProfile routes - index 
    path('auth/', include("apps.authentication.urls")), # Auth routes - login / register
]
# ERROR HANDLERS
handler404 = 'apps.views.page_not_found'
handler403 = 'apps.views.page_forbidden'
handler500 = 'apps.views.server_error'
