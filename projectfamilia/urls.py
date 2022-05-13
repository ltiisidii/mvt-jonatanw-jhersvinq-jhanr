from django.contrib import admin
from django.urls import path
from appfamiliares.views import mis_familiares


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mis_familiares),
]
