"""
URL configuration for DjangoWEb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import include, path
import DjangoWEb.views as v



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('BookingSite.urls')),
    path('', v.indexs, name='LogoPage'),
    path('landingPage/', v.mainpage, name='mainPage'),
    path('flightfav/', v.flightfav, name='flightfav'),
    path('AboutUs/', v.AboutUs, name='AboutUs'),
    path('basicInfo/', v.basicInfo, name='basicInfo'),
    path('customerAbout/', v.customerAbout, name='customerAbout'),
    path('customerProfile/', v.customerProfile, name='customerProfile'),
    path('customerService/', v.customerService, name='customerService'),
    path('flightDetails/', v.flightDetails, name='flightDetails'),
    path('flightFinalPayment/', v.flightFinalPayment, name='mainPage'),
    path('flightReservation/', v.flightReservation, name='mainPage'),
    path('flightSearch/', v.flightSearch, name='mainPage'),
    path('flightTicket/', v.flightTicket, name='mainPage'),
    path('helpAndFeedback/', v.helpAndFeedback, name='mainPage'),
    path('hotelBooking/', v.hotelBooking, name='mainPage'),
    path('hotelF/', v.hotelF, name='mainPage'),
    path('hotelFull/', v.hotelFull, name='mainPage'),
    path('hotelInfo/', v.hotelInfo, name='mainPage'),
    path('hotelReservation/', v.hotelReservation, name='mainPage'),
    path('hotelS/', v.hotelS, name='mainPage'),
    path('hotelSandR/', v.hotelSandR, name='hotelSandR'),
    path('login/', v.login, name='mainPage'),
    path('pageError/', v.pageError, name='mainPage'),
    path('paymentInfo/', v.paymentInfo, name='mainPage'),
    path('profilePreference/', v.profilePreference, name='mainPage'),
    path('register/', v.register, name='mainPage'),
    path('settingProfile/', v.settingProfile, name='mainPage'),
    path('trackBooking/', v.trackBooking, name='mainPage'),
    path('footer/', v.footer, name='footer'),
    path('base/', v.base, name='base'),
    
    
]
