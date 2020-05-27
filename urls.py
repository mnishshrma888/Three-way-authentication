from django.urls import path
from. import views


urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('forgot_pswrd',views.forgot_pswrd,name='forgot_pswrd'),
    path('signup',views.signup,name='signup'),
    path('capture',views.capture,name='capture'),
    path('otp_gen',views.otp_gen,name='otp_gen'),
    path('otp_gen2', views.otp_gen2, name='otp_gen2'),
    path('otp',views.otp,name='otp'),
    path('otp1',views.otp1,name='otp1'),
    path('face', views.face, name='face'),
    path('click', views.click, name='click'),
    path('about', views.about, name='about'),


]