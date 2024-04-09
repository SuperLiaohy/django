from django.urls import path

from . import views

urlpatterns =[
    path('',views.toLogin_view),
    # path('index/',views.Login_view1),
    path('index/',views.Login_view),
    path('toregister/',views.toRegister_view),
    # path('register/',views.Register_view1),
    path('register/',views.Register_view),
]
