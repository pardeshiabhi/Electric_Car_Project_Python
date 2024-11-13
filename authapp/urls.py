from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('login',views.handlelogin,name="handlelogin"),
    path('logout',views.handlelogout,name="handlelogout"),
    path('contact',views.contact,name="contact"),
    path('EVcars',views.Booking,name="Booking"),
    path('profile',views.profile,name="profile"),
    path('Rental',views.Rental,name="Rental"),
    path('services',views.services,name="services"),
    path('about',views.about,name="about"),
    path('team',views.team,name="team"),
 
]