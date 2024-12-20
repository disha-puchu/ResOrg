from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from todonoteapp import views

urlpatterns = [
    path('createtodo/', views.createtodo),
    path('edittodo/<tdid>/', views.edittodo),
    path('checktodo/<tdid>/', views.checktodo),
    path('deletetodo/<tdid>/', views.deletetodo),
    path('editnote/', views.editnote),
    path('clearnote/', views.clearnote),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)