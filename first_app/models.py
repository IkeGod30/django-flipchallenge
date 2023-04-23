from django.db import models

# Create your models here.
class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    user_name = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name}, {self.last_name} was born on {self.dob}"
        


