from django.contrib import admin
from django.urls import path
# import rvsapp.views
# import login.views
from rvsapp import views as rvs
from login import views as log


admin.site.site_header = "Admin JaGs"
admin.site.site_title = "Django Admin"
admin.site.index_title = "Welcome to Admin JaGs"


urlpatterns = [
    # path('', views.user, name="user"),
    path('', rvs.jags, name="jags"),
    path('home', rvs.home, name="home"),
    path('form', rvs.form, name="form"),
    path('about', rvs.about, name="about"),
    path('service', rvs.service, name="service"),
    path('contact', rvs.contact, name="contact"),
    path('login', log.loginuser, name="login"),
    path('logout', log.logoutuser, name="logout"),
    path('main', log.main, name="main"),
    path('admin/', admin.site.urls),
   

]
