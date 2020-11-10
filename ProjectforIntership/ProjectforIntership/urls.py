from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls'), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
