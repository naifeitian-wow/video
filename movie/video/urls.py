from django import urls
from django.urls import path
from .views import list,detail,video

app_name='list'
urlpatterns=[
    path('detail/<type>/<int:id>/',detail,name='detail'),
    path('<type>/<type2>/<country>/<year>/<int:page_num>/',list,name='list'),
    path('<type>/',list,name='type'),
    path('<type>/video/<int:id>/',video,name='video'),
]