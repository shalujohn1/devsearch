from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

# def projects(request):
#     return HttpResponse('here are our products')
#
# def project(request,pk):
#      return HttpResponse('single project' + ' ' + str(pk))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
    # path('projects/',projects, name="projects"),
    # path('project/<str:pk>/',project, name="project"),
    path('users/', include('users.urls')),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
