FATMUG Django Developer Assesment : 

#  MODELS :

           . Vendor :  Represents a vendor with fields such as name, contact details, address, and vendor code.
           . PurchaseOrder :  Represents a purchase order with fields like PO number, vendor (foreign key to Vendor), order date, delivery date, items, quantity, status, quality rating, issue date, and acknowledgment date.
           . HistoricalPerformance : Stores historical performance data for vendors, including fields like vendor (foreign key to Vendor), date, on-time delivery rate, quality rating average, average response time, and fulfillment rate.  
           
    ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/6b9ec17f-c715-408c-ab16-63219d4f7d43)


# Serializers :

                VendorSerializer: Serializes and deserializes Vendor objects.
                PurchaseOrderSerializer: Serializes and deserializes PurchaseOrder objects.
                HistoricalPerformanceSerializer: Serializes and deserializes HistoricalPerformance objects.

    ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/ac50ecb2-b613-467e-9435-aaa820f63358)

# Views:

        . Various API views (create_vendor, list_vendor, vendor_detail, create_purchase, list_purchase, purchase, acknowledgepurchase, vendorperformance) that handle HTTP requests and perform CRUD operations on the models.
        . API endpoints are decorated with @api_view and @permission_classes to define the allowed methods and required permissions (in this case, IsAuthenticated).

# Authentication:

        .Token-based authentication using TokenAuthentication from Django REST Framework.
        .Permissions set using IsAuthenticated.

# Helper Functions:

        .Functions to calculate vendor performance metrics like on-time delivery rate, quality rating average, average response time, and fulfillment rate.

# STEPS : 

->  Create an empty folder 

->  Open with VS Code make sure you have installed the latest version of Python and Django 

->  install django rest_framework 

->  create a new project : django-admin startproject vendorManagement

->  create a app inside this vendorManagement Project : python manage.py startapp vndordetails 

->  Register the app and the rest_framework under the installed apps in setting.py file 

->  create different models as given in the questions 

->  create serializer of each model 

-> Go to the views.py file wirte the logic to GET and POST the data 

-> Registered this in the urls.py file 

-> Use JWT Tokenauthentication so that only authenticated person is allowed to GET and POST the data.

# SCREEN SHOTS OF WORKING VENDOR API ON VS-CODE EXTENSION THUNDER-CLIENT :
   
    . No unauthorized Person is allowed to GET and POST the vendor details 
    
        ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/021a5994-21e8-463c-ad80-a7a957a4a86d)

    . Generate a new TOKEN by passing the username and password of USERS. 

    ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/cd108c38-b17e-48a2-bcb2-fe9e70d8b0b7)

    . Paste this new token in AUTH Bearer Token and then try to POST the data 

    ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/7a9d7d4b-1af9-4c74-bd40-cef96b120ac7)

    .![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/5bf650af-45cf-4a90-bac4-635d1d7f45db)

    . We cannot post the data with the same vendor id 

    ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/f8dd8322-9549-4822-b925-12b9d3c2f58b)

    . Now GET the details of all the vendors 

    ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/95c3ade3-9e35-4bc7-89b5-b32ecd0894b4)

    . GET the details of vendor with the id 
    ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/6865fb56-1efe-4d71-8178-c57cff67f00e)

     . If there is no vendor present in the specific id then it shows error 
     ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/9ef70a89-68fc-4ab6-be43-aa0085f72668)

     . Update the data using PUT method

     ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/641f9673-872b-4ba3-8e59-d61bfc470f38)

     . GET the data of same vendor we will find the the data will updated successfully 

     ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/88535551-8fa4-4774-93bf-8959fef0f4d3)

     . DELETE the data of the vendor 
     
     ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/8fd4d25f-33d6-449b-9efa-9e55e328270d)
     
     ![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/ef5f3004-c1da-4847-992c-e20cda2b49d6)




 # NOW CREATE AN API FOR PURCHASE ORDER TRACKING AND THIS PURCHASE ODRER API IS LINK WITH THE  VENDOR  :

. Doing the same as vendor , generate new token , because token is only valid for some period of time . 

. POST the Purchasing Order data 

. This Purchase order data is link with the vendor so it first check the id is present on the vendor or not , if it is ot present then it shows error message .

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/afe11a47-3f9c-4c13-9ce5-4653e66d3852)

.if the vendor id present in the vendor then it POST the data .

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/ee054a3b-5e6d-4122-a71a-62ab82ff06c2)

.GET the list of all the data 

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/3f2525e0-592c-4041-87c2-0588130a306c)

. GET the data of specific user 

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/e7427bf4-d3d1-43c8-bcf5-ce449c212cb8)

. if there is no purchase order created with the id then it showw message: invalid id 

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/78266920-c08e-460c-88a4-16e13117d000)

. Update the existing data using PUT method 

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/e4a4bd75-7ab7-48ea-ba5b-ceb9fc7b91d7)

.Data Updated successfully 

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/ac6442b5-c11f-4374-8589-af2589a1af59)

. Delete the purchase order using DELETE method 
![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/1fdde309-07ce-4943-a5a4-565f7a093e73)

. if the id is not there it shows error 
![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/3dd8a173-550c-4114-a4bd-bf5fd652f4c6)


# Vendor Performance Evaluation 

. Doing the same as vendor , generate new token , because token is only valid for some period of time .

. POST the Purchasing Order data : 

. check first that the vendor with the given id present on the vendor or not , if not present gives error
![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/2173dd58-ec0e-4b91-a552-e51aee79f517)


. if the vendor is present in the vendor data , then its POST the successfully 
![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/6633c46c-5cad-4ec5-9cd8-185af54dac84)

. if there is no purchase order found in the purchase_data , then it shows msg 'purchase order not found '

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/ac0ce0b4-ed72-4718-bae6-cbeecd1162d6)

. if there is purchase of the vendor then is shows the data 
![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/964c1d37-d69b-4560-ab26-701730a1fb94)



# also it save the data in Backend 
![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/1b44dcfb-f89f-4177-ac09-ae85892c22d1)

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/108ac774-0a3c-4867-9509-e9c3b7476682)

![image](https://github.com/prateeksingh4435/VendorManagementSystem/assets/128826031/45e2bd27-e203-458c-a744-b69ee1e38dda)






































