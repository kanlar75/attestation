from django.urls import path
from rest_framework.routers import DefaultRouter

from electronics_network.apps import ElectronicsNetworkConfig
from electronics_network.views import CompanyDetailAPIView, \
    CompanyCreateAPIView, \
    CompanyUpdateAPIView, CompanyListAPIView, CompanyDeleteAPIView, \
    ContactViewSet, ProductViewSet

app_name = ElectronicsNetworkConfig.name

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path("company/<int:pk>/", CompanyDetailAPIView.as_view(),
         name="company_detail"),
    path("company/delete/<int:pk>/", CompanyDeleteAPIView.as_view(),
         name="company_delete"),
    path("companies/", CompanyListAPIView.as_view(), name="company_list"),
    path("company/", CompanyCreateAPIView.as_view(), name="company_create"),
    path("company/update/<int:pk>/", CompanyUpdateAPIView.as_view(),
         name="company_update"),
] + router.urls
