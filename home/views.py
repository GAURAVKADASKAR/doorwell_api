from django.shortcuts import render
from home.serializer import *
from rest_framework.decorators import APIView,api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
# Create your views here.

class register_user(APIView):

    def post(self,request):
        user=User.objects.filter(username=request.data.get('username'))
        if user.exists():
            return Response({'status':404,'error':'user already exists'})
        
        serlializer=registration_serializer(data=request.data)
        if serlializer.is_valid():
            serlializer.save()
            return Response({'status':200,'message':'success'})
        else:
            return Response({'status':404,'message':serlializer.errors})
    

class login_user(APIView):

    def post(self,request):
        username=request.data.get('username')
        passcode=request.data.get('passcode')
        
        user=authenticate(username=username,password=passcode)
        if user is None:
            return Response({'status':404,'error':'invalid username or password'})
        request.session['username']=username
        return Response({'status':200,'message':'success'})
    

class Enter_the_item(APIView):
    
    def post(self,request):
        serializer=Doorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':200,'message':'success'})
        return Response({'status':404,'message':'Invalid data ','error':serializer.errors})

class get_door_details(APIView):

    def get(self,request,name):
        obj=door_item.objects.get(item_name=name)
        serializer=Doorserializer(obj)
        obj1=sub_catagories.objects.filter(item_name=name)
        serializer_sub=subcategory_serializer(obj1,many=True)
        return Response({'statua':200,'Item':serializer.data,'sub_item':serializer_sub.data})
    
class get_price(APIView):

    def post(self,request):
        item_name=request.data.get('item_name')
        sub_item=request.data.get('sub_item')
        size=request.data.get('size')
       
        try:
            obj=sub_catagories.objects.get(sub_item=sub_item,item_name=item_name,item_size=size)
            if obj:
                return Response({'status':200,'message':obj.item_price})
     
                
        except sub_catagories.DoesNotExist:
               obj1=sub_catagories.objects.filter(item_size__gt=size,sub_item=sub_item,item_name=item_name).order_by('item_size').first()
               if obj1:
                     return Response({'status':200,'message':obj1.item_price})
               else:
                    return Response({'status':404,'error':'itemee not found'})

                
                