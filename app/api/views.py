from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from app.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from django.http import Http404

# Create your views here.


# def index(request):
#     return HttpResponse("Hi")
# @api_view()
# def userlist(request):
    # profile = Users.objects.all()
    # serializer = UserSerializer(profile, many=True)
    # return Response(serializer.data) 



class UserList(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,pk=None):
        if pk:
            try:
                users = Users.objects.get(pk=pk)
            except Users.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = UserSerializer(users)    
        else:
            users = Users.objects.all()
            serializer = UserSerializer(users, many=True)  
        return Response(serializer.data) 

class UserDetail(APIView):
    def get(self,request,pk=None):
        try:
            users = Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(users)      
        return Response(serializer.data) 

    def put(self,request,pk=None):
        users = Users.objects.get(pk=pk)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# order generation function, still working on it 
    def post(self, request,pk=None):
        user = User.objects.get(pk=pk)
        serializer = FoodorderSerializer(data=request.data)
        if serializers.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
            
    def delete(self,request,pk=None):
        users = Users.objects.get(pk=pk)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    def login(request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Users.objects.get(username=username, password=password)
        except Users.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CategoryList(APIView):
    def get(self,request):
        categories = Categorylist.objects.all()
        serializer = CategorylistSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = CategorylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryDetail(APIView):
    def get(self,request,pk=None):
        try:
            categories = Categorylist.objects.get(pk=pk)
            serializer = CategorylistSerializer(categories)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Categorylist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk=None):
        categories = Categorylist.objects.get(pk=pk)
        serializer = CategorylistSerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk=None):
        categories = Categorylist.objects.get(p=pk)
        categories.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OrderList(APIView):
    def get(self,request,pk=None):
        if pk:
            try: 
                orderlist = Foodorder.objects.get(pk=pk)
            except Foodorder.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = FoodorderSerializer(orderlist)
        else:
            orderlist = Foodorder.objects.all()
            serializer = FoodorderSerializer(orderlist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FoodorderpostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class OrdList(generics.ListCreateAPIView):
    queryset = Foodorder.objects.all()
    serializer_class = FoodorderpostSerializer
    



# if pk:
#             try:
#                 users = Users.objects.get(pk=pk)
#             except Users.DoesNotExist:
#                 return Response(status=status.HTTP_404_NOT_FOUND)
#             serializer = UserSerializer(users)    
#         else:
#             users = Users.objects.all()
#             serializer = UserSerializer(users, many=True)  
#         return Response(serializer.data) 


# try:
#             categories = Categorylist.objects.get(pk=pk)
#             serializer = CategorylistSerializer(categories)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Categorylist.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)