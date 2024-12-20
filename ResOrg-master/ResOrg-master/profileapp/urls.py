from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from profileapp import views

urlpatterns = [
    path('', views.profile),
    path('editprofile/', views.editprofile),
    path('changepassword/', views.changepassword),
    path('deleteaccount/', views.deleteaccount),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)