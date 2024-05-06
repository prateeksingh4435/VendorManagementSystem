from .models import Vendor,PurchaseOrder , HistoricalPerformance
from rest_framework import serializers



class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = ['id','name' , 'contact_details','address','vendor_code']
        
        
        
class PurchaseOrderSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = PurchaseOrder
        fields = '__all__'     
        
    
class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields ='__all__'
        
        