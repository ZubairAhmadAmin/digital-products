from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Category, Product
from .serializer import ProductSerializer, CategorySerializer


class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CategoryDetailView(APIView):
    
    def get_category(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return False
        
    
    def get(self, request, pk):
        category = self.get_category(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        category = self.get_category(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk):
        category = self.get_category(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# class CategoryDetailView(APIView):

#     def get(self, request, pk):
#         try:
#             category = Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = CategorySerializer(category, context={'request': request})
#         return Response(serializer.data)


# class ProductListView(APIView):

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True, context={'request': request})
#         return Response(serializer.data)


# class ProductDetailView(APIView):

#     def get(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = ProductSerializer(product, context={'request': request})
#         return Response(serializer.data)


# class FileListView(APIView):

#     def get(self, request, product_id):
#         files = File.objects.filter(product_id=product_id)
#         serializer = FileSerializer(files, many=True, context={'request': request})
#         return Response(serializer.data)


# class FileDetailView(APIView):

#     def get(self, request, product_id, pk):
#         try:
#             file = File.objects.get(pk=pk, product_id=product_id)
#         except File.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = FileSerializer(file, context={'request': request})
#         return Response(serializer.data)