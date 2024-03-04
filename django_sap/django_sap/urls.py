"""django_sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # users app
    path('', include('applications.api.urls')),
    path('layout/',include('web.layout.urls')),
    # File manager View
    #Ecommerce
    path('ecommerce/',include("web.ecommerce.urls")),
    #Crypto
    path('crypto/',include('web.crypto.urls')),
    #Email
    path("email/",include("web.e_mail.urls")),
    #Invoices
    path('invoices/',include('web.invoices.urls')),
    #Projects
    path('projects/',include('web.projects.urls')),
    #Tasks
    path('tasks/',include('web.tasks.urls')),
    #Blog
    path('blog/',include('web.blog.urls')),
    #Blog
    path('contacts/',include('web.contacts.urls')),
    #Authencation
    path('authentication/',include('web.authentication.urls')),
    #Utility
    path('utility/',include('web.utility.urls')),
    #Components
    path('components/',include('web.components.urls')),
]