from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)

    def __str__(self):
        return self.email

class Carbooking(models.Model):
    FullName=models.CharField(max_length=25)
    email=models.EmailField()
    Gender=models.CharField(max_length=25)
    Phonenumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    Selectcar=models.CharField(max_length=200)
    selectfeatures=models.CharField(max_length=200)
    refrence=models.CharField(max_length=55)
    address=models.TextField()
    paymentstatus=models.CharField(max_length=55,blank=True,null=True)
    price=models.IntegerField(max_length=55,blank=True,null=True)
    Duedate=models.DateTimeField(blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.FullName

class CarType(models.Model):
    cartitle=models.CharField(max_length=25)
    Features=models.CharField(max_length=25)
    Value=models.IntegerField(max_length=25)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.cartitle
    
class Selectcarbrand(models.Model):
    carbrand=models.CharField(max_length=25)
    price=models.IntegerField(max_length=100)

    def __int__(self):
        return self.id
    
class Carrenting(models.Model):
    FullName=models.CharField(max_length=25)
    Email=models.EmailField()
    Gender=models.CharField(max_length=25)
    Phonenumber=models.CharField(max_length=12)
    DOB=models.CharField(max_length=50)
    Selectcar=models.CharField(max_length=200)
    selectfeatures=models.CharField(max_length=200)
    Refrence=models.CharField(max_length=55)
    Address=models.TextField()
    Paymentstatus=models.CharField(max_length=55,blank=True,null=True)
    Price=models.IntegerField(max_length=55,blank=True,null=True)
    Duedate=models.DateTimeField(blank=True,null=True)
    Timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.FullName
class rentingType(models.Model):
    Cartitle=models.CharField(max_length=50)
    Features=models.CharField(max_length=50)
    Value=models.IntegerField(max_length=25)
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.Cartitle
    
class carbrand(models.Model):
    Carbrand=models.CharField(max_length=50)
    price=models.IntegerField(max_length=100)

    def __int__(self):
        return self.id

class Services(models.Model):
    title=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='gallery')

    def __int__(self):
        return self.id

class About(models.Model):
    Title=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='gallery')

    def __int__(self):
        return self.id

class Team(models.Model):
    Teamname=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='gallery')

    def __int__(self):
        return self.id


