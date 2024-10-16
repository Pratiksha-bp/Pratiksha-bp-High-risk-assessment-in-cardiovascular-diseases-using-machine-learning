from django.db import models
from django.utils import timezone




class Users(models.Model): 
    # mail = models.CharField(max_length = 50) 
    # username = models.CharField(max_length = 50)
    # password = models.CharField(max_length = 50) 
    # phonenumber = models.IntegerField() 

    fname = models.CharField(max_length = 50) 
    lname = models.CharField(max_length = 50) 
    username = models.CharField(max_length = 50) 
    email = models.CharField(max_length = 50) 
    phone = models.CharField(max_length = 50) 
    pass1 = models.CharField(max_length = 50) 
    pass2 = models.CharField(max_length = 50) 
    address = models.CharField(max_length = 50) 

    # class Meta: 
    #     db_table = "users"
    def __str__(self):
        return self.username


