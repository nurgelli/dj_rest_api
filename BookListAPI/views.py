# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view, APIView
# from rest_framework import viewsets
# from rest_framework.views import APIView 


from rest_framework import generics
from .models import BookItem
from .serializers import BookItemSerializers


# Create your views here.

class BookItemViews(generics.ListCreateAPIView):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializers
class SingleBookItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializers






#1. Function based
# @api_view(['GET', 'POST'])
# def books(request):
#     return Response('list of the books', status=status.HTTP_200_OK)


#2. Class based
# class Book():
#     @staticmethod
#     @api_view(['PUT', 'GET'])
#     def books(request):
#         return Response({'message': 'list of orders'}, status=status.HTTP_200_OK)

# #3. with APIView
# class BookView(APIView):
#     # def put(self, request, pk):
#     #     return Response({'title': request.data.get('title')}, status.HTTP_200_OK)
#     def get(self, request):
#         author = request.GET.get('author')
#         if(author):
#             return Response({'message': 'List of the books by ' + author}, status.HTTP_200_OK) #http://127.0.0.1:8000/api/books/?author=Tolstoy
#         return Response({"message": "LIST OF THE BOOKS"}, status.HTTP_200_OK)
#     def post(self, request):
#           return Response({"Awtory": request.data.get('title')}, status.HTTP_201_CREATED)  # {"title": "Gogol"}

# class Book(APIView):    
#     def get(self, request, pk):
#         return Response({"message": "single book with id " + str(pk)}, status=status.HTTP_200_OK)
#     def put(self, request, pk):
#         return Response({"Ady": request.data.get('title'), "Familiyasy": request.data.get('surname')}, status.HTTP_200_OK) #{"title": "Gogol"}

#Viewset
# class BookLibrary(viewsets.ViewSet):
#     def list(self, request):
#         return Response({'message': "All books"}, status.HTTP_200_OK)
#     def create(self, request):
#         return Response({'message': "All books"}, status.HTTP_200_OK)
#     def update(self, request, pk=None):
#         return Response({'message': "All books" + str(pk)}, status.HTTP_200_OK)
#     def retrive(self, request, pk=None):
#         return Response({'message': "All books"}, status.HTTP_200_OK)
#     def partial_update(self, request, pk=None):
#         return Response({'message': "All books"}, status.HTTP_200_OK)
#     def destroy(self, request, pk=None):
#         return Response({'message': "All books"}, status.HTTP_200_OK)

