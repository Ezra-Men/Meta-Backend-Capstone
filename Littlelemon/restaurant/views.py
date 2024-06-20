from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import response
from rest_framework.decorators import permission_classes



def index (request):
     return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
 queryset = MenuItem.objects.all()
serializer_class = MenuItemSerializer
permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
 queryset = MenuItem.objects.all()
serializer_class = MenuItemSerializer

class BookingViewSet(ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes =['IsAuthenticated']

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = (permissions.IsAuthenticated)

@api_view()

# @authentication_classes([TokenAuthentication])
def msg (request):
  return response ({"message":"This view is protected"})