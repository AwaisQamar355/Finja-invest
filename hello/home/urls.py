from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.home , name = 'home.html'),
    path('home.html',views.home , name = 'home.html'),
    path('product.html',views.product , name = 'product.html'),
    path('portfolio.html',views.portfolio , name = 'portfolio.html'),
    path('fmcg.html',views.fmcg , name = 'fmcg.html'),
    path('agriculture.html',views.agriculture , name = 'agriculture.html'),
    path('store.html',views.store , name = 'store.html'),
    path('security.html',views.security , name = 'security.html'),
    path('license.html',views.license , name = 'license.html'),
    path('shariah.html',views.shariah , name = 'shariah.html'),
    path('faqs.html',views.faqs , name = 'faqs.html'),
    path('login.html',views.loginuser , name = 'login.html'),
    path('logout.html',views.logoutuser , name = 'logout.html'),
    path('signup.html',views.signup , name = 'signup.html'),

]
   