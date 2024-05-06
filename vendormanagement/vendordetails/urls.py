from django.contrib import admin
from django.urls import path , include 
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
    
    path('vendors/create',views.create_vendor,name='createvendor'),
    path('vendors/list',views.list_vendor,name='listvendor'),
    path('vendors/<int:id>',views.vendor_detail,name="vendordetail"),
    
    #Purchasedata 
    path('purchase/create',views.create_purchase,name="createpurchase"),
    path('purchase/list',views.list_purchase,name="listpurchase"),
    path('purchase/<int:id>', views.purchase,name='purchase'),
    
    #historicalPerformance 
    path('vendors/<int:id>/acknowledge',views.acknowledgepurchase,name="acknowledgepurchase"),
    path('vendors/<int:id>/performance',views.vendorperformance,name="vendorperformance")
    
    
    
    
]