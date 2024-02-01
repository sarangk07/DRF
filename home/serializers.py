from rest_framework import serializers
from .models import Person,Car
from django.contrib.auth.models import User




#validators
def starts_with_capital(value):
    if value['0'].lower():
        raise serializers.ValidationError("name starts with capital letter")

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100,validators=[starts_with_capital])
    email = serializers.EmailField()
    password = serializers.CharField()
    
    
    #field level Validation
    def validate_username(self,value):
        if value['0'].lower():
            raise serializers.ValidationError("name starts with capital letter") 
        return value    
    
    
    #object level Validation
    def validate(self,data): 
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('username is already taken')
        if data['email']:
            if User.objects.filter(username = data['email']).exists():
                raise serializers.ValidationError('email is already taken')
        return data
    
    
    
    
    
    
    
    
    def create(self,validated_data):
        print(validated_data)
        user = User.objects.create(username = validated_data['username'],email = validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data                
    






class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['model']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class PeopleSerializer(serializers.ModelSerializer):
    
    car = CarSerializer()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1
    
    def validate(self, data):
        if data['age'] > 200:
            raise serializers.ValidationError("age should be lower than 200")
        elif 'name' in data and not isinstance(data['name'], str):
            raise serializers.ValidationError("name must be  charters no numbers and simpels")
        return data