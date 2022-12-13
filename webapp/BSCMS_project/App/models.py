from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# creating Model for store adminuser other details


class AppAdmin_Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adminMobile = models.IntegerField(null=True)
    registerDate = models.DateTimeField(auto_now=True, null=True)

    def __str__(self) -> str:
        return str(self.user.username) + "-" + str(self.adminMobile)

# creating baby sistter model


class BabySitters(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    mobileNo = models.IntegerField(null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=100, null=True)
    languagesKnown = models.TextField(null=True)
    babySittersExp = models.CharField(max_length=100, null=True)
    profilePic = models.ImageField(null=True)
    certificate = models.CharField(max_length=300, null=True)
    descreption = models.TextField(null=True)
    regDate = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)


class Contact(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    mobile = models.IntegerField(null=True)
    massege = models.TextField(null=True)
    enquiryDate = models.DateField(auto_now_add=True)
    isRead = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.first_name)


class Enrollment(models.Model):
    enrollNumber = models.IntegerField(null=True)
    yourName = models.CharField(max_length=100, null=True)
    phoneNumber = models.IntegerField(null=True)
    alternateNumber = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    childName = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    childGender = models.CharField(max_length=10, null=True)
    programName = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.IntegerField(null=True)
    city = models.CharField(max_length=100, null=True)

    landmark = models.CharField(max_length=300, null=True)
    enrollmentDate = models.DateTimeField(auto_now_add=True, null=True)
    remark = models.CharField(max_length=400, null=True)
    status = models.CharField(max_length=50, null=True)
    remarkDate = models.DateField(auto_now=True)

    def enrollMent_number(self):
        self.enrollNumber = 60551148 + self.id

    def __str__(self) -> str:
        return str(self.enrollNumber) + "-" + str(self.yourName)


class Service(models.Model):
    service = models.CharField(max_length=100, null=True)
    serviceDetail = models.CharField(max_length=100, null=True)
    service_img = models.ImageField(null=True)
    creationsDate = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.service)


class Subscriber(models.Model):
    email = models.EmailField(null=True)
    dateOfSub = models.DateField(auto_now=True, null=True)

    def __str__(self) -> str:
        return str(self.email)


class AboutUs(models.Model):
    heading = models.CharField(max_length=200,null=True)
    details = models.TextField(null=True)

    def __str__(self) -> str:
        return "about_us " + str(self.id) 
class Contact_us(models.Model):
    address = models.TextField(null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)

    def __str__(self) -> str:
        return "contact_us" + str(self.id)