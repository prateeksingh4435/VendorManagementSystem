from django.shortcuts import render
from .serializers import VendorSerializer , PurchaseOrderSerializer ,HistoricalPerformanceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vendor ,PurchaseOrder , HistoricalPerformance
from django.db.models import Avg
from . import models
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_vendor(request):
    data  = request.data
    serilaizer = VendorSerializer(data=request.data)
    if not serilaizer.is_valid():
        return Response({'status':'400','msg':'something went wrong','error':serilaizer.errors})
    serilaizer.save()
    
        
    return Response({'status':'200','data':serilaizer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_vendor(request):
    data = Vendor.objects.all()
    serilaizer = VendorSerializer(data , many=True)
    return Response({'status':200,'payload':serilaizer.data})


@api_view(['GET' ,'PUT','DELETE'])
@permission_classes([IsAuthenticated])
def vendor_detail(request,id):
    
    try:
        vendor  = Vendor.objects.get(pk=id)
    except Exception as e:
        return Response({'status':400,'msg':'Invalid id '})
    
    
    if request.method == "GET":
        serializer = VendorSerializer(vendor)
        return Response({'status':200 , 'payload':serializer.data})
    
    
    elif request.method == "PUT":
        serializer = VendorSerializer(vendor, request.data)
        if not serializer.is_valid():
            return Response({'status':400,'payload':serializer.errors,'msg':'incorrect data or invalid id '})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'msg':"data updated Successfully"})
    
    elif request.method == "DELETE":
        try:
            vendor.delete()
            return Response({'status':200,'msg':'Data Deleted Successfully'}) 
        except Exception as e:
            return Response({'status':200,'msg':'Invalid data'})
            
    
    
#PurchaseOrder


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_purchase(request):
    vendor_id = request.data.get('vendor')

    try:
        vendor = Vendor.objects.get(pk = vendor_id)
    except Exception as e :
        return Response({'status':400,"MSG":"There is no Vendor with this id"})
    
    serializer = PurchaseOrderSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':400,'error':serializer.errors})
    
    serializer.save()
    return Response({'status':400,'payload':serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_purchase(reqeust):
    purchase_detail = PurchaseOrder.objects.all()
    serializer = PurchaseOrderSerializer(purchase_detail,many=True)
    return Response({'status':200 , 'payload':serializer.data})


@api_view(['PUT','DELETE','GET'])
@permission_classes([IsAuthenticated])
def purchase(request,id):
    try:
        purchase_detail = PurchaseOrder.objects.get(id=id)
        
    except Exception as e:
        return Response({'status':400 ,'Message':'Invalid id'})
    
    if request.method == "GET":
        serializer = PurchaseOrderSerializer(purchase_detail)
        return Response({'status':200,'payload':serializer.data})
    
    
    elif request.method == "PUT":
        try:
            purchase_detail = PurchaseOrder.objects.get(id=id)
        except Exception as e:
            return Response({'status':400 , 'payload':'Invalid id'})
        
        vendor_id  = request.data.get('vendor')
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
        except Exception as E:
            return Response({'status':400 ,'msg':'no vendor is present with this id '})

        serializer = PurchaseOrderSerializer(purchase_detail,data = request.data)
        if not serializer.is_valid():
            return Response({'status':400,'error':serializer.errors,'msg':'something Went Wrong'})
        serializer.save()
        return Response({'status':400 ,'payload':serializer.data , 'msg':'data updated successfully'})
    
    
    elif request.method == "DELETE":
        try:
           
            purchase_detail.delete()
            return Response({'status':200,'msg':'data deleted successfully'})
        except Exception as e:
            return Response({'status':200,'msg':'Invalid data'})
            
            
            
            
#HistoricalPerformance

from django.utils import timezone

# Update Acknowledgment Endpoint
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def acknowledgepurchase(request, id):
    try:
        purchaseorder = PurchaseOrder.objects.get(id=id)
    except PurchaseOrder.DoesNotExist:
        return Response({'status': 404, 'msg': 'Purchase order not found'})
    
    vendor_id  = request.data.get('vendor')
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Exception as E:
        return Response({'status':400 ,'msg':'no vendor is present with this id '})
    

    purchaseorder.acknowledgment_date = timezone.now()
    purchaseorder.save()
    

    # Calculate average_response_time
    average_response(purchaseorder.vendor)
    serializer = HistoricalPerformanceSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
         return Response({'status': 200, 'error': serializer.errors})

    return Response({'status': 200, 'msg': 'Acknowledgment data updated successfully'})

#  average response time
def average_response(vendor):
    purchase_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    total_time = sum((p.acknowledgment_date - p.issue_date).total_seconds() for p in purchase_orders)
    response_time = total_time / purchase_orders.count()
    vendor.response_time = response_time
    vendor.save()

# Vendor Performance Endpoint
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vendorperformance(request, id):
    
    try:
        vendor = Vendor.objects.get(id=id)
    except Vendor.DoesNotExist:
        return Response({'status': 404, 'msg': 'Vendor not found'})
    
    try:
        purchase_order = PurchaseOrder.objects.get(id=id)
    except Exception as e:
        return Response({'status': 404, 'msg': 'Purchase order of this id is not found'})
        
    deliveryrate = delivery_rate(vendor)
    quality_rating = qualityrating(vendor)
    fulfilment_rate = fulfilmentrate(vendor)

    response_time = average_response(vendor)
 
    performance_data = {
        'delivery_rate': delivery_rate(vendor),
        'quality_rating': qualityrating(vendor),
        'response_time': vendor.response_time,
        'fulfilment_rate': fulfilmentrate(vendor)
    }
    
   
    return Response({'status': 200, 'data': performance_data})

#  on-time delivery rate
def delivery_rate(vendor):
    complete_order = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
    timecompleteorder = PurchaseOrder.objects.filter(vendor=vendor, status='completed', delivery_date__lte=timezone.now()).count()
    if complete_order == 0:
        return 0
    return (timecompleteorder / complete_order) * 100

#  quality rating average
def qualityrating(vendor):
    c_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull=False)
    if c_orders.exists():
        return c_orders.aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
    return 0

#  fulfilment rate
def fulfilmentrate(vendor):
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    successful_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed', issue_date__isnull=False, acknowledgment_date__isnull=False).count()
    if total_orders == 0:
        return 0
    return (successful_orders / total_orders) * 100

       
                
    
    

    
    
    
        
        
    
