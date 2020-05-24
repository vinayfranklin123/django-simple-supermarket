"""marketplace URL Configuration

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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account.views import (
    registration_view,
    logout_view,
    login_view,
    ProfileView,
)
from storage.views import (
    search_view,
    dashboard_view,
    brand_view,
    category_view,
    product_view,
    stockin_view,
    stockout_view,
    brand_add_view,
    category_add_view,
    # product_add_view,
    # stockin_add_view,
    # stockout_add_view,
)

urlpatterns = [
    path('', login_view, name='login'),
    path('index/', search_view, name='index'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/brands', brand_view, name='brand'),
    path('dashboard/categories', category_view, name='category'),
    path('dashboard/products', product_view, name='product'),
    path('dashboard/stockin', stockin_view, name='stockin'),
    path('dashboard/stockout', stockout_view, name='stockout'),
    path('dashboard/brand_add', brand_add_view, name='brand_add'),
    path('dashboard/category_add', category_add_view, name='category_add'),
    # path('dashboard/product_add', product_add_view, name='product_add'),
    # path('dashboard/stockin_add', stockin_add_view, name='stockin_add'),
    # path('dashboard/stockout_add', stockout_add_view, name='stockout_add'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
