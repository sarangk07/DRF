from home.views import index,person,login,LoginAPI,RegisterAPI,PersonAPI,PeopleViewSet
from django.urls import path,include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('peopleapi',PeopleViewSet,basename='people')
urlpatterns = router.urls



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view()),
    path("login/",LoginAPI.as_view()),
    path("index/", index),
    path("person/", person),
    
    path("persons/", PersonAPI.as_view()),
    path('gettoken/', obtain_auth_token),
]
