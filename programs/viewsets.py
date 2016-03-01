from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from .models import ProgramService, Program, ProgramReview, HealthCondition
from habits.models import Habit
from challenges.models import Challenge
from hobbys.models import Hobby
from routines.models import Routine
from .serializers import ProgramListSerializer, ProgramServiceListSerializer, ProgramReviewListSerializer, ProgramServiceUpdateSerializer, HealthConditionListSerializer

class ProgramListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Program.objects.all()
    serializer_class = ProgramListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            Program.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # urls: /programs & /programs?health_condition_id='id'
    def list(self, request, *args, **kwargs):
        health_condition = request.GET.get('health_condition_id',None)
        queryset= self.queryset
        if health_condition is not None:
            queryset = self.queryset.filter(health_condition_id=health_condition)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    # url: programs/id/subscribed_programs    gives the all the programs that user has subscribed to.
    @detail_route()
    def subscribed_programs(self, request, id):
        #print id
        user =  id
        data = Program.objects.raw('SELECT * FROM programs_program WHERE id IN (SELECT program_id_id '
                                'FROM programs_programservice WHERE user_id_id=%s)',[user])
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # url: programs/subscribed_habits?health_condition_id='id'  gives the all the reviews that user has given.
    @list_route()
    def subscribed_habits(self,request):
        health_condition = request.GET['health_condition_id']
        program_id = self.queryset.filter(health_condition_id=health_condition)[0].id
        data = Habit.objects.raw('SELECT * FROM habits_habit WHERE id IN (SELECT program_id_id '
                                'FROM programs_programcomponent WHERE (program_id_id=%s AND component_type=%s)',[program_id,'HA'])
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # url: programs/subscribed_hobbys?health_condition_id='id'  gives the all the reviews that user has given.
    @list_route()
    def subscribed_hobbys(self,request):
        health_condition = request.GET['health_condition_id']
        program_id = self.queryset.filter(health_condition_id=health_condition)[0].id
        data = Hobby.objects.raw('SELECT * FROM hobbys_hobby WHERE id IN (SELECT program_id_id '
                                'FROM programs_programcomponent WHERE (program_id_id=%s AND component_type=%s)',[program_id,'HA'])
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # url: programs/subscribed_routines?health_condition_id='id'  gives the all the reviews that user has given.
    @list_route()
    def subscribed_routines(self,request):
        health_condition = request.GET['health_condition_id']
        program_id = self.queryset.filter(health_condition_id=health_condition)[0].id
        data = Routine.objects.raw('SELECT * FROM routines_routine WHERE id IN (SELECT program_id_id '
                                'FROM programs_programcomponent WHERE (program_id_id=%s AND component_type=%s)',[program_id,'HA'])
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # url: programs/subscribed_challenges?health_condition_id='id'  gives the all the reviews that user has given.
    @list_route()
    def subscribed_challenges(self,request):
        health_condition = request.GET['health_condition_id']
        program_id = self.queryset.filter(health_condition_id=health_condition)[0].id
        data = Challenge.objects.raw('SELECT * FROM challenges_challenge WHERE id IN (SELECT program_id_id '
                                'FROM programs_programcomponent WHERE (program_id_id=%s AND component_type=%s)',[program_id,'HA'])
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class ProgramServiceListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = ProgramService.objects.all()
    serializer_class = ProgramServiceListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            ProgramService.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user = request.GET.get('user_id',None)
        queryset= self.queryset
        if user is not None:
            queryset = self.queryset.filter(user_id=user)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class ProgramServiceUpdateViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = ProgramService.objects.all()
    serializer_class = ProgramServiceUpdateSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)



class ProgramReviewListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = ProgramReview.objects.all()
    serializer_class = ProgramReviewListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            ProgramReview.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        program = request.GET.get('program_id',None)
        queryset= self.queryset
        if program is not None:
            queryset = self.queryset.filter(program_id=program)
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


class HealthConditionListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = HealthCondition.objects.all()
    serializer_class = HealthConditionListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            HealthCondition.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)