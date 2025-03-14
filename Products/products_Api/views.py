from django.shortcuts import render
from .seralizers import ProductSeralizer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Products
from rest_framework.pagination import PageNumberPagination
# Create your views here.

#Products create  api view
@api_view(['POST'])
def add_product(request):
    serializer=ProductSeralizer(data=request.data)
    if serializer.is_valid():
       serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Update the products api view
#PUT is used to update the entrie record in db
#PATCH is used to update the few partial elements in db
@api_view(['PUT','PATCH'])
def update_product(request,pid):
    try:
        items=Products.objects.get(product_id=pid)
    except Products.DoesNotExist:
        return Response({"Error":"Product not found"},status=status.HTTP_404_NOT_FOUND)
    
    seralizer = ProductSeralizer(items,data=request.data,partial=True)
    if seralizer.is_valid():
        seralizer.save()
        return Response({"message":"Product updated sucessfully"},status=status.HTTP_201_CREATED)
    

#View products based on ids
@api_view(['GET'])
def view_product(request,pid):
    try:
        item=Products.objects.get(product_id=pid)
        seralizer=ProductSeralizer(item)
        return Response(seralizer.data, status=status.HTTP_200_OK)
    except Products.DoesNotExist:
        return Response({"message":"Product not found with that id"})
    
#GET All producst in db 
@api_view(['GET'])
def all_products(request):
    pagenation =PageNumberPagination()#set pagination 10 records per page
    pagenation.page_size=10
    
    items = Products.objects.all().order_by('product_id')
    pages=pagenation.paginate_queryset(items,request)#here applying pagination
    serializer=ProductSeralizer(pages,many=True)#seralize the pagination results
     
    return pagenation.get_paginated_response(serializer.data)#return response as paginations
    
    
    

    
    