from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    path('About-Rajokari-Institute-of-technology', views.aboutpage, name='aboutpage'),
    path('Faculty-of-Rajokari-Institute-of-technology', views.facultypage, name='facultypage'),
    path('Admission/Admissions-Proccedure-for-Rajokari-Institute-of-technology', views.admissionspage, name='admissionspage'),
    path('Admission/Fee-Structure', views.feepage, name='feepage'),
    path('Academics/Courses-Offered', views.coursespage, name='coursepage'),
    path('Gallery-of-Rajokari-Institute-of-technology', views.gallerypage, name='gallerypage'),
    path('Downloads/Forms', views.formspage, name='formspage'),
    path('signup', views.signuppage, name='signup'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logout, name="logout"),    
]
