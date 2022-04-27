"""redFlags URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

import flags.views as app

api_v1 = r'api/v1/'

router = DefaultRouter()


router.register(api_v1 + r'tenders',
                app.TenderViewSet,
                basename='tender')
router.register(api_v1 + r'lots',
                app.LotViewSet,
                basename='lot')
router.register(api_v1 + r'entities',
                app.EntityViewSet,
                basename='entity')
router.register(api_v1 + r'bids',
                app.BidViewSet,
                basename='bid')
router.register(api_v1 + r'classifiers',
                app.ClassifierViewSet,
                basename='classifier')
router.register(api_v1 + r'irregularities',
                app.IrregularityViewSet,
                basename='irregularity')
router.register(api_v1 + r'flags',
                app.FlagViewSet,
                basename='flag')
router.register(api_v1 + r'flag_data',
                app.FlagDataViewSet,
                basename='flag_data')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', app.MainPageView.as_view(), name='home'),
    path('details/<str:pk>/', app.FlagDetailsView.as_view(), name='flag-details')
] + router.urls
