from django.db import models

# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=50,primary_key=True)
    lname=models.CharField(max_length=50,default="")
    phoneno=models.CharField(max_length=50,default="")
    email=models.EmailField()
    password=models.CharField(max_length=50,default="")
    def __str__(self):
        return self.fname

    def isExists(self):
        if Contact.objects.filter(email = self.email):
            return True

        return  False
   