from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from .models import RoutineService, Routine, RoutineReview
from .serializers import RoutineListSerializer, RoutineServiceListSerializer, RoutineReviewListSerializer, RoutineServiceUpdateSerializer

class RoutineListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Routine.objects.all()
    serializer_class = RoutineListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            Routine.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoutineServiceListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = RoutineService.objects.all()
    serializer_class = RoutineServiceListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            RoutineService.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoutineServiceUpdateViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = RoutineService.objects.all()
    serializer_class = RoutineServiceUpdateSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)



class RoutineReviewListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = RoutineReview.objects.all()
    serializer_class = RoutineReviewListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            RoutineReview.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # urls: /routinereviews & /routinereviews?routine_id='id'
    def list(self, request, *args, **kwargs):
        routine = request.GET.get('routine_id',None)
        queryset= self.queryset
        if routine is not None:
            queryset = self.queryset.filter(routine_id=routine)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # url: routinereviews/id/user_reviews    gives the all the reviews that user has given.
    @detail_route()
    def user_reviews(self, request, id):
        #print id
        user =  id
        data = self.queryset.filter(user_id=user)
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # url: routinereviews/reviews?user_id='id'  gives the all the reviews that user has given.
    @list_route()
    def reviews(self,request):
        user = request.GET['user_id']
        data = self.queryset.filter(user_id=user)
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
