from telnetlib import STATUS
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Users
from .serializers import UsersSerializer
from django.contrib.auth.hashers import make_password


class UsersViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @action(methods=['post'], detail=False)
    def login(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            dt = self.get_serializer_class()(user).data
            return Response({'result':dt})
        else:
            return Response({'result': 'user is not registered'})

    
    @action(methods=['post'], detail=False)
    def register(self, request):
        username = request.data['username']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        birthday = request.data['birthday']
        phone = request.data['phone']
        staff = request.data['staff']
        address = request.data['address']
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({'result': f'{username} already taken!'})
        else:
            user = Users.objects.create(username=username, password=make_password(password), first_name=first_name, last_name=last_name, birthday=birthday, phone=phone, staff=staff, address=address)
            dt = self.get_serializer_class()(user).data
            return Response({'result':dt})

    def create(self, request):
        return Response({"detail": "Method \'POST\' not allowed."})

    def destroy(self, request, pk=None):
        return Response({"detail": "Method \'DELETE\' not allowed."})

    @action(methods=['get'], detail=False)
    def by_staff(self, request):
        st = request.GET['st']
        data = Users.objects.filter(staff=st)
        dt = self.get_serializer_class()(data, many=True).data
        
        return Response({'result':dt})
