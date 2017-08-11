from django.db import models

# Create your models here.

class new_user(models.Model):
	firstname = models.CharField(max_length=60,blank=False,null=False)
	lastname = models.CharField(max_length=60,blank=False,null=False)
	gender = models.BooleanField('gender:')
	mobilenum = models.IntegerField()
	email = models.EmailField()
	password = models.TextField(blank=False, max_length=30)
	cpassword = models.TextField(blank=False, max_length=30)

class courier_d(models.Model):
	Sname = models.CharField(max_length=60,blank=False,null=False)
	Sloc = models.CharField(max_length=60,blank=False,default='-')
	smobno = models.IntegerField(default=0)
	smail = models.EmailField(default='-')
	saddr = models.CharField(max_length=60,blank=False,default='-')
	city = models.CharField(max_length=60,blank=False,default='-')
	pin = models.IntegerField(default=0)
	Rname = models.CharField(max_length=60,blank=False,null=False,default='-')
	Dloc = models.CharField(max_length=60,blank=False,default='-')
	rmobno = models.CharField(max_length=60,blank=False,null=False,default=0)
	
class bushire(models.Model):

	user_name=models.CharField(max_length=60,blank=False,default='-')
	user_mail=models.EmailField()
	phone=models.IntegerField()
	bus_t = models.CharField(max_length=10,default='Non-A/C')
	pickup=models.CharField(max_length=60,blank=False,default='-')
	from_date=models.CharField(max_length=60,blank=False,default='-')
	to_date=models.CharField(max_length=60,blank=False,default='-')
	no_of_people=models.IntegerField()
	city= models.CharField(max_length=30)
	bustype=models.CharField(max_length=30)

class Destination(models.Model):
	name = models.CharField(max_length=100)
	count = models.PositiveIntegerField(default=0)


class Bus(models.Model):
	name = models.CharField(max_length=100)
	number = models.IntegerField()
	places = models.TextField()
	avail = models.CharField(max_length=8)

class Register(models.Model):
	username=models.CharField(max_length=300)
	password = models.CharField(null=True,max_length=20)


	
