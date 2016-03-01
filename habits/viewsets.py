from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from .models import HabitService, Habit, HabitReview
from .serializers import HabitListSerializer, HabitServiceListSerializer, HabitReviewListSerializer, HabitServiceUpdateSerializer

class HabitListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Habit.objects.all()
    serializer_class = HabitListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            Habit.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # url: habits/id/subscribed_habits    gives the all the habits that user has subscribed to.
    @detail_route()
    def subscribed_habits(self, request, id):
        #print id
        user =  id
        data = Habit.objects.raw('SELECT * FROM habits_habit WHERE id IN (SELECT habit_id_id '
                                'FROM habits_habitservice WHERE user_id_id=%s)',[user])
        print data
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class HabitServiceListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HabitService.objects.all()
    serializer_class = HabitServiceListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            HabitService.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # url: habitservices?user_id='id'   gives the all the habits that user has subscribed to.
    def list(self, request, *args, **kwargs):
        user = request.GET.get('user_id',None)
        queryset= self.queryset
        if user is not None:
            queryset = self.queryset.filter(user_id=user)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class HabitServiceUpdateViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HabitService.objects.all()
    serializer_class = HabitServiceUpdateSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)



class HabitReviewListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HabitReview.objects.all()
    serializer_class = HabitReviewListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            HabitReview.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        habit = request.GET.get('habit_id',None)
        queryset= self.queryset
        if habit is not None:
            queryset = self.queryset.filter(habit_id=habit)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)