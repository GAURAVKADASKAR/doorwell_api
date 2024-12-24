from django.db import models
from django.contrib.auth.models import User
# register model



class registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    full_name=models.CharField(max_length=200)
    shop_name=models.TextField()
    address=models.TextField()
    mobile_number=models.TextField()
    username=models.TextField()
    email=models.EmailField(default='')
    passcode=models.TextField()
    
    
    def __str__(self):
        return self.full_name


class door_item(models.Model):
    item_name=models.CharField(primary_key=True,max_length=200)
    item_image=models.FileField(upload_to='door_image')

    def __str__(self):
        return self.item_name


class sub_catagories(models.Model):
    item_name=models.ForeignKey(door_item,on_delete=models.SET_NULL,null=True,blank=True)
    sub_item=models.TextField()
    item_size=models.TextField()
    item_price=models.TextField()

    def __str__(self):
        return self.sub_item
    

