from django.contrib import admin
from django.urls import path, include
from todolist.urls import todolist_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include(todolist_urls))
]
