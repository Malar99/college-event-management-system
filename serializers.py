from rest_framework import serializers
from .models import login
from .models import register
from .models import event


class registerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=register 
        fields=('first_name','last_name','gender','age','email')
class loginserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=login
        fields=('username','password')     
class eventserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=event
        fields=('eventname','venue','eventdate','eventphoneNo','eventimage')

     