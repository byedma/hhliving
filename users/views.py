from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
import json
from rest_framework.response import Response
from rest_framework import status
from .forms import RegistrationForm
from rest_framework import views
from .serializers import HUserAuthSerializer
# Create your views here.


def index(request):
    return render_to_response('index.html')

def home(request):
    return render_to_response('home.html')

def user_landing_view(request):
    return render_to_response('landing.html')

class LoginView(views.APIView):

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = HUserAuthSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print request.POST
        if form.is_valid():
            print "Good"
    else:
        form = RegistrationForm()

    return render(request, 'users/registration_form.html', {'form': form})


