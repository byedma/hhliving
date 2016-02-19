from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from .models import HobbyService, Hobby, HobbyReview
from .serializers import HobbyListSerializer, HobbyServiceListSerializer, HobbyReviewListSerializer, HobbyServiceUpdateSerializer

class HobbyListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Hobby.objects.all()
    serializer_class = HobbyListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            Hobby.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HobbyServiceListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HobbyService.objects.all()
    serializer_class = HobbyServiceListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            HobbyService.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HobbyServiceUpdateViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HobbyService.objects.all()
    serializer_class = HobbyServiceUpdateSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)



class HobbyReviewListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HobbyReview.objects.all()
    serializer_class = HobbyReviewListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            HobbyReview.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def list(self, request, *args, **kwargs):
        hobby = request.GET.get('hobby_id',None)
        queryset= self.queryset
        if hobby is not None:
            queryset = self.queryset.filter(hobby_id=hobby)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    @detail_route()
    def user_reviews(self, request, id):
        #print id
        user =  id
        data = self.queryset.filter(user_id=user)
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    @list_route()
    def reviews(self,request):
        user = request.GET['user_id']
        data = self.queryset.filter(user_id=user)
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
