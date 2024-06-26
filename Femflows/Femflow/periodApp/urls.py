from django.urls import path
from . import views 


urlpatterns = [
    path('',views.home, name='period-home'),
    path('about/',views.about, name='period-about'),
    path('login/',views.loginPage, name='period-login'),
    path('signup/',views.signup, name='period-signup'),
    path('main/',views.main, name='period-main'),
    path('after/',views.after, name='period-after'),
    path('logout/',views.logoutPage, name='period-logout'),
]
