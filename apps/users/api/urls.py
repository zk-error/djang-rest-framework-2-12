from django.urls import path
from  apps.users.api.api import UserApiView,user_detail_view
urlpatterns = [
    path('usuario/',UserApiView,name='usuario_api'),
    path('usuario/<int:pk>',user_detail_view,name='user_detail_view')
]
