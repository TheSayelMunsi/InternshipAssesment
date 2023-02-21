from rest_framework import serializers
from .models import *

class Client_Table_Serializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = client_table
        fields = '__all__'
class Work_Table_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Work_table
        fields = '__all__'
class Artist_Table_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Artist_table
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        # extra_kwargs = {'password': {'write_only': True}}