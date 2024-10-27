from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter



urlpatterns = [
    path('book-items/', views.BookItemViews.as_view()),
    path('book-items/<int:pk>', views.SingleBookItemView.as_view())
]



#1. for Function based view
# urlpatterns = [
#     path('books', views.books)
# ]


#2. Class based
# urlpatterns = [
#     path('books', views.Book.books)
# ]


#3. with APIView
# urlpatterns = [
#     # path('books', views.books),
#     path('books/', views.BookView.as_view()),
#     path('books/<int:pk>', views.Book.as_view()),
#     path('books', views.BookLibrary.as_view({
#         'get': "list",
#         "post": "create"
#     })),
#     path('books/<int:pk>', views.BookLibrary.as_view(
#         {
#             'get': "retrive",
#             'put': 'update',
#             'patch': 'partial_update',
#             'delete': 'destroy'
#         }
#     ))
# ]


#SimpleRouter
# router = SimpleRouter(trailing_slash=False)
# router.register('books', views.BookLibrary, basename='books')
# urlpatterns = router.urls

#DefaultRouter
# router = DefaultRouter(trailing_slash=False)
# router.register('books', views.BookLibrary, basename='books')
# urlpatterns = router.urls