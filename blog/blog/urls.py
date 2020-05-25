"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import home_view
from home.views import sign_in_view
from home.views import sign_up_view
from home.views import forgot_password_view
from home.views import patent_one_view
from home.views import patent_second_view
from home.views import patent_third_view
from home.views import patent_fourth_view
from home.views import patent_fifth_view
from home.views import contact_view
from home.views import who_we_are_view
from home.views import our_vision_view
from home.views import submit
from home.views import result_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home_view'),
    path('sign_in/',sign_in_view,name='sign_in_view'),
    path('sign_up/',sign_up_view,name='sign_up_view'),
    path('forgot_password/',forgot_password_view,name='forgot_password_view'),
    path('patent_one/',patent_one_view,name='patent_one_view'),
    path('patent_second/',patent_second_view,name='patent_second_view'),
    path('patent_third/',patent_third_view,name='patent_third_view'),
    path('patent_fourth/',patent_fourth_view,name='patent_fourth_view'),
    path('patent_fifth/',patent_fifth_view,name='patent_fifth_view'),
    path('contact/',contact_view,name='contact_view'),
    path('who_we_are/',who_we_are_view,name='who_we_are_view'),
    path('our_vision/',our_vision_view,name='our_vision_view'),
    path('submit/', submit, name='submit'),
    path('result/', result_view, name='result_view'),
]


