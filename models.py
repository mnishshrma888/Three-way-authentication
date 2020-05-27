from django.db import models

# Create your models here.
class person(models.Model):
    user_id=models.AutoField
    first_name=models.CharField(max_length=50, default="")
    last_name=models.CharField(max_length=50, default="")
    user_name1=models.CharField(max_length=100, default="")
    password=models.CharField(max_length=60, default="")
    address=models.CharField(max_length=150, default="")
    mobile=models.CharField(max_length=60, default="")
    city=models.CharField(max_length=20, default="")
    gender=models.CharField(max_length=10, default="")
    images=models.ImageField(upload_to="newapp/static/images", default="")

    def __str__(self):
        return self.user_name1