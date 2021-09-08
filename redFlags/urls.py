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

import flags.views as turnip_app

api_v1 = r'api/v1/'

router = DefaultRouter()

router.register(api_v1 + r'tenders',
                turnip_app.TenderViewSet,
                basename='tender')
router.register(api_v1 + r'lots',
                turnip_app.LotViewSet,
                basename='lot')
router.register(api_v1 + r'entities',
                turnip_app.EntityViewSet,
                basename='entity')
router.register(api_v1 + r'bids',
                turnip_app.BidViewSet,
                basename='bid')
router.register(api_v1 + r'classifiers',
                turnip_app.ClassifierViewSet,
                basename='classifier')
router.register(api_v1 + r'irregularities',
                turnip_app.IrregularityViewSet,
                basename='irregularity')
router.register(api_v1 + r'flags',
                turnip_app.FlagViewSet,
                basename='flag')


urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
