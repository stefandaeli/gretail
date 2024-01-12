from django.urls import path
from .views import *

urlpatterns =[
    path('index',index,name='index'),
    
    #login
    path('v_owners',v_owners,name='v_owners')
]