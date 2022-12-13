#from django.contrib import admin
from django.urls import  path #,include

from . import views


# urlpatterns = [
#     path('mesligues/', include('mesligues.urls')),
#     path('admin/', admin.site.urls),
# ]

app_name = 'mesligues'
urlpatterns = [
    
    path('', views.index, name='index'),
    path('liste_participants/', views.liste_participants, name='liste_participants'),
    path('liste_participants/participant/', views.participant, name='participant'),
    path('liste_matchs/', views.liste_matchs, name='liste_matchs'),
    path('liste_matchs/match/', views.match, name='match'),
    path('classement/', views.classement, name='classement'),
]