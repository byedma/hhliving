from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route
from .models import ChallengeService, Challenge, ChallengeReview
from .serializers import ChallengeListSerializer, ChallengeServiceListSerializer, ChallengeReviewListSerializer, ChallengeServiceUpdateSerializer, NewChallengeServiceSerializer

class ChallengeListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Challenge.objects.all()
    serializer_class = ChallengeListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            Challenge.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # url: challenges/id/subscribed_challenges    gives the all the challenges that user has subscribed to.
    @detail_route()
    def subscribed_challenges(self, request, id):
        #print id
        user =  id
        data = Challenge.objects.raw('SELECT * FROM challenges_challenge WHERE id IN (SELECT challenge_id_id '
                                'FROM challenges_challengeservice WHERE user_id_id=%s)',[user])
        print data
        serializer = self.serializer_class(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class ChallengeServiceListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = ChallengeService.objects.all()
    serializer_class = ChallengeServiceListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            ChallengeService.objects.create(**serializer.validated_data)
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


class NewChallengeServiceViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = ChallengeService.objects.all()
    serializer_class = NewChallengeServiceSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            ChallengeService.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChallengeServiceUpdateViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = ChallengeService.objects.all()
    serializer_class = ChallengeServiceUpdateSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        if self.request.method == 'PUT':
            return (permissions.AllowAny(),)

        if self.request.method == 'DELETE':
            return (permissions.AllowAny(),)



class ChallengeReviewListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = ChallengeReview.objects.all()
    serializer_class = ChallengeReviewListSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            ChallengeReview.objects.create(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print serializer.errors

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        challenge = request.GET.get('challenge_id',None)
        queryset= self.queryset
        if challenge is not None:
            queryset = self.queryset.filter(challenge_id=challenge)
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
