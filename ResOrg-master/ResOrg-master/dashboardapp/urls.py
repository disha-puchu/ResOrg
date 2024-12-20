from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboardapp import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('dashboard/<uid>/', views.dashboard),
    path('dashboard/<uid>/', include('topicapp.urls')),
    path('dashboard/<uid>/profile/', include('profileapp.urls')),

    # path('editprofile/<uid>/', views.editprofile),
    # path('changepassword/<uid>/', views.changepassword),
    # path('deleteaccount/<uid>/', views.deleteaccount),

    path('creategroup/<uid>/', views.creategroup),
    path('dashboard/<uid>/renamegroup/<gid>/', views.renamegroup),
    path('dashboard/<uid>/deletegroup/<gid>/', views.deletegroup),

    path('createtopic/<uid>/', views.createtopic),
    path('dashboard/<uid>/renametopic/<gid>/<tid>/', views.renametopic),
    path('dashboard/<uid>/deletetopic/<gid>/<tid>/', views.deletetopic),

    path('dashboard/<uid>/todonote/', include('todonoteapp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)