from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from rest_framework.views import APIView
from rest_framework import viewsets,status
from home.serializers import PeopleSerializer,RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from django.core.paginator import Paginator


class RegisterAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data = data)
        
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message': serializer.errors
            },status.HTTP_400_BAD_REQUEST)
            
        serializer.save()
        
        return Response({'status':True , 'message':'user created'})
        



class LoginAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message': serializer.errors
            },status.HTTP_400_BAD_REQUEST)
            
        user = authenticate(username = serializer.data['username'],password = serializer.data['password'])
        print(user,'userrrrr')
        token, _ = Token.objects.get_or_create(user=user)
        print(token,'tokennnnn')
        return Response({'status':True , 'message':'user logedin','token': str(token)})






from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class PersonAPI(APIView):
    def get(self,request):
        obj = Person.objects.all()
        page = request.GET.get('page',1)
        page_size = 2
        paginator = Paginator(obj,page_size)
        
        
        try:
            current_page = paginator.page(page)
        except PageNotAnInteger:
            current_page = paginator.page(1)
        except EmptyPage:
            current_page = paginator.page(paginator.num_pages)

        serializer = PeopleSerializer(current_page, many=True)
        return Response(serializer.data)

        
    def post(self,request):
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    def put(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
        
        
    def patch(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data=data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    
    def delete(self,request):
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({"message" : 'person deleted!'})











@api_view(['GET','POST'])
def index(request):
    courses = {
        'course_name':'Python_FullStack',
        'learn':['Django','React','PSQL','ORM','DRF','Redux','Bootstrap'],
        'source':'Internet'
    }
    if request.method == 'POST':
        data = request.data
        print(data)
        print("you click post")
        return Response(courses)
    else :
        print("you click get")
        return Response(courses)
    
@api_view(['POST'])   
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        return Response({"message" : 'success'})
    return Response(serializer.errors)
       
    

@api_view(['GET','POST','PUT','PATCH' , 'DELETE'])
def person(request):
    if request.method == 'GET':
        # GET to retrieve data from the API
        obj = Person.objects.all()
        serializer = PeopleSerializer(obj , many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # POST to send data to the API and create a new resource
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PUT':
        #PUT not support partical update
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':
        #PATCH support partical update
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj, data=data , partial=True)
        
        #obj = old data from database,  data=new data from the server, partial = supports partial updates
        
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({"message" : 'person deleted!'})





class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
    
    
    
@action(detail=True,methods=['post']) 
def send_mail_to_person(self,request):
    return Response(
        {
            'status':True,
            'message':'email sent success!'
        }
    )  



