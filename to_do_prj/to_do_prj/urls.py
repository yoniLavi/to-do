"""to_do_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tasks.views import get_tasks, add_task, edit_task, task_detail, update_status

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_tasks, name='get_tasks'),
    url(r'^add$', add_task, name='add_task'),
    url(r'^(?P<id>\d+)/edit$', edit_task, name='edit_task'),
    url(r'^(?P<id>\d+)', task_detail, name='task_detail'),
    url(r'^update/(?P<id>\d+)$', update_status, name='update_status')
]
