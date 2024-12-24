from rest_framework.serializers import ModelSerializer
from home.models import *


class registration_serializer(ModelSerializer):
    class Meta:
        model=registration
        fields="__all__"

    def create(self, validated_data):
        username=validated_data['username']
        passcode=validated_data['passcode']
        email=validated_data['email']
        mobile_number=validated_data['mobile_number']
        shop_name=validated_data['shop_name']
        full_name=validated_data['full_name']
        address=validated_data['address']


        obj=User.objects.create(
            username=username
        )
        obj.set_password(passcode)
        obj.save()

        obj_register=registration.objects.create(
            username=username,
            passcode=passcode,
            email=email,
            mobile_number=mobile_number,
            shop_name=shop_name,
            full_name=full_name,
            address=address
        )
        obj_register.save()

        return validated_data




class Doorserializer(ModelSerializer):
    class Meta:
        model=door_item
        fields="__all__"
    

class subcategory_serializer(ModelSerializer):
    class Meta:
        model=sub_catagories
        fields="__all__"
        