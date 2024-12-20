from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from topicapp import views

urlpatterns = [
    path('topic/<tid>/', views.topic),

    path('topic/<tid>/createsection/', views.createsection),
    path('topic/<tid>/renamesection/<sid>/', views.renamesection),
    path('topic/<tid>/deletesection/<sid>/', views.deletesection),

    path('topic/<tid>/addresource/web/', views.add_weblink),
    path('topic/<tid>/addresource/yt/', views.add_ytlink),

    path('topic/<tid>/deletelink/<rid>/', views.deletelink),
    path('topic/<tid>/editweblink/<sid>/<rid>/', views.editweblink),
    path('topic/<tid>/editytlink/<sid>/<rid>/', views.editytlink),
    
    path('topic/<tid>/addresource/<filetype>/', views.addfile),
    path('topic/<tid>/deletefile/<rid>/', views.deletefile),
    path('topic/<tid>/editfile/<rid>/', views.editfile),

    path('topic/<tid>/todonote/', include('todonoteapp.urls')),

    # path('topic/<tid>/search/', views.search_videos),

    # path('topic/<tid>/groupbytype/', views.groupbytype),
    path('topic/<tid>/view/<rid>/', views.view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)