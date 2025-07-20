from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('submit/',views.submit,name='submit'),
    path('regards/',views.thanks,name='thanks'),
    path('track/',views.track,name='track'),
    path('facultysupport/',views.faculty,name='faculty'),
    path('about/',views.about,name='about')
    
]