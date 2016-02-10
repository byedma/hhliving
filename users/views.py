from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
