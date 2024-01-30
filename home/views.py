from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST'])
def index(request):
    courses = {
        'course_name':'Python_FullStack',
        'learn':['Django','React','PSQL','ORM','DRF','Redux','Bootstrap'],
        'source':'Internet'
    }
    if request.method == 'POST':
        print("you click post")
        return Response(courses)
    else :
        print("you click get")
        return Response(courses)



