"""hhliving URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from users import urls as users_urls
from hhliving import settings

from rest_framework import routers
from users import viewsets as users_viewsets
from habits import viewsets as habits_viewsets
from hobbys import viewsets as hobbys_viewsets
from routines import viewsets as routines_viewsets
from challenges import viewsets as challenges_viewsets
from programs import viewsets as programs_viewsets
from users import views as users_views


router = routers.DefaultRouter()
router.register(r'users', users_viewsets.HUserViewSet)
router.register(r'edit_users', users_viewsets.HUserEditViewSet)
router.register(r'circles', users_viewsets.CircleListViewSet)
router.register(r'edit_circles', users_viewsets.CircleEditViewSet)
router.register(r'circlemembers', users_viewsets.CircleMemberListViewSet)
router.register(r'edit_circlemembers', users_viewsets.CircleMemberEditViewSet)
router.register(r'habits', habits_viewsets.HabitListViewSet)
router.register(r'habitservices', habits_viewsets.HabitServiceListViewSet)
router.register(r'edit_habitservices', habits_viewsets.HabitServiceUpdateViewSet)
router.register(r'habitreviews', habits_viewsets.HabitReviewListViewSet)
router.register(r'hobbys', hobbys_viewsets.HobbyListViewSet)
router.register(r'hobbyservices', hobbys_viewsets.HobbyServiceListViewSet)
router.register(r'edit_hobbyservices', hobbys_viewsets.HobbyServiceUpdateViewSet)
router.register(r'hobbyreviews', hobbys_viewsets.HobbyReviewListViewSet)
router.register(r'routines', routines_viewsets.RoutineListViewSet)
router.register(r'routineservices', routines_viewsets.RoutineServiceListViewSet)
router.register(r'edit_routineservices', routines_viewsets.RoutineServiceUpdateViewSet)
router.register(r'routinereviews', routines_viewsets.RoutineReviewListViewSet)
router.register(r'challenges', challenges_viewsets.ChallengeListViewSet)
router.register(r'challengeservices', challenges_viewsets.ChallengeServiceListViewSet)
router.register(r'edit_challengeservices', challenges_viewsets.ChallengeServiceUpdateViewSet)
router.register(r'challengereviews', challenges_viewsets.ChallengeReviewListViewSet)
router.register(r'programs', programs_viewsets.ProgramListViewSet)
router.register(r'programservices', programs_viewsets.ProgramServiceListViewSet)
router.register(r'edit_programservices', programs_viewsets.ProgramServiceUpdateViewSet)
router.register(r'programreviews', programs_viewsets.ProgramReviewListViewSet)
router.register(r'healthconditions', programs_viewsets.HealthConditionListViewSet)

#router.register(r'^edit_users/(?P<pk>[0-9]+)$/edit_circles/(?P<pk>[0-9]+)$', users_viewsets.CircleMemberViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^api/v1/login/$', users_views.LoginView.as_view(), name='login'),
    url(r'^api/v1/logout/$', users_views.LogoutView.as_view(), name='logout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)