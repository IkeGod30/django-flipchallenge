from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(max_length=50) # validators=[MaxValueValidator(1999-9-20)]
    email = models.EmailField(unique=True)
    user_name = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name} is registered."
    
# class QuesModel (models.Model):
#     question = models.CharField(max_length=200, null=True)
#     op1 = models.CharField(max_length=200, null=True)
#     op2 = models.CharField(max_length=200, null=True)
#     op3 = models.CharField(max_length=200, null=True)
#     op4 = models.CharField(max_length=200, null=True)
#     ans = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.question
        

# class SignIn(models.Model):
   # user_name = models.CharField(unique=True, max_length=50)
   # password = models.CharField(max_length=50)
    
    # def __str__(self):
        # return f"Hello {self.user_name}, you are now logged in."
