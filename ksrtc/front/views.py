from django.shortcuts import render
from django.http import HttpResponse
from front.models import *
# Create your views here.

def adhome(request):
	if 'logged_in' in request.session and request.session['logged_in']==True:
		all_places = Destination.objects.values()
	else:
		return render(request,"admin.html")	
	
	return render(request,"adhome.html",{ 'page':all_places } )

def adminuser(request):
	if 'logged_in' in request.session and request.session['logged_in']==True:
		all=new_user.objects.all()
		return render(request,"details.html",{'data':all})
	else:
		return render(request,"admin.html")

def courier_request(request):
	return render(request,"courier.html",{})

def courier_res(request):
	print request.POST
	receivname = request.POST['Rname']
	sendname = request.POST.get('Sname', False);
	sendloc = request.POST['Sloc']
	sendmob = request.POST['smobno']
	destloc = request.POST['Dloc']
	sendpin = request.POST['pin']
	sendaddr = request.POST['saddr']
	dphone = request.POST['rmobno']
	senmail = request.POST['smail']
	cor = courier_d(rmobno=dphone,Rname = receivname,Sname = sendname,Sloc = sendloc,pin = sendpin,smobno = sendmob,Dloc = destloc,smail = senmail,saddr = sendaddr)
	print 'hai'
	cor.save()
	return render(request,"courier_response.html",{})


def user_login(request):
	return render(request,"user.html",{})

def user_response(request):
	
	print request.POST
	#fname = request.POST['firstname']
	fname = request.POST.get('firstname', False);
	lname = request.POST['lastname']
	gndr =request.POST['gender']
	mob = request.POST['mobilenum']
	mob=int(mob)
	em=request.POST['email']
	nwuser=new_user(firstname = fname, lastname = lname, gender = gndr, mobilenum = mob, email=em)
	fpas=request.POST['password']
	cpas=request.POST['cpassword']
	print fpas
	if fpas==cpas:
		nwuser.save()
		return render(request,"user_response.html",{'firstname':fname,'lastname':lname,'gender':gndr,'mobilenum':mob,'email':em})
	return render(request,"user.html",{'error':'password does not match!'})

	#nw_cor=courier_detail(Rname = receivname,Sname = sendname,Sloc = sendloc,smobno = sendmob,Dloc = destloc,city = sendcity,saddr = sendaddr,smail = senmail,pin = sendpin,hname = housenam)

def f2(request):
	return render(request,"signup.html",{})

def ebushire(request):
	Hire_city= ['Thiruvananthapuram','Kollam','Pathanamthitta','Alappuzha','Kottayam','idukki','Ernakulam','Thrissur','Palakkad','Malappuram','Kozhikode','Wayanad','Kannur','Kasargod']
	bus=['City ordinary','Cityfast','Fast PASSENGER/LSFP','SUPERFAST PASSENGER','SUPER EXPRESS''SUPER DELUXE/SEMI SLEEPER','LUXURY/HI-TECH/AC'
,'VOLVO','MULTIAXLE VOLVO']
	
	return render(request,"hire.html",{'hire':Hire_city,'data':bus})


def ebushiresubmit(request):
	data = request.POST
	print data
	inst = bushire(bus_t=data['bus_type'],
		user_name=data['user_name'],
		user_mail=data['user_mail'],
		phone=data['phone'],
		pickup=data['pickup'],
		from_date=data['from_date'],
		to_date=data['to_date'],
		no_of_people=data['no_of_people'],
		city=data['city'],
		bustype=data['bus'],
		)
	inst.save()
	return render(request,"success.html")

def home(request):
	return render(request,'homepage.html',{})

def homepbus(request):
	return render(request,'homepbus.html',{})

def homepcourier(request):
	return render(request,'homepcourier.html',{})


def search(request):
	post_data = request.POST
	source,destination = post_data['search'],post_data['track']
	search_string = '.*%s.*%s.*'%(source,destination)
	result = Bus.objects.filter(places__iregex=search_string)
	data = []
	days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
	for d in result:
		avail_str = d.avail
		places = d.places.split(',')
		avail_days = []
		for i in xrange(7):
			if avail_str[i]=='1':
				avail_days.append( days[i] )

		data.append(
			{
				'name' : d.name,
				'src' : places[0],
				'route' : '->'.join(places),
				'dest' : places[-1],
				'avail' : ','.join(avail_days),
				'number' : d.number
			})
		x,created = Destination.objects.get_or_create(name=destination)
		x.count+=1
		x.save()


	return render(request,"search_result.html",{'data':data})

def abt(request):
	return render(request,"about.html")

def depot(request):
	return render(request,'depots.html',{})

def fare(request):
	return render(request,'fare.html',{})

#admin

#0. login
def login(request):
	return render(request,"admin.html")

def my(request):
	u = request.POST['username']
	p = request.POST['password']
	
	valid_user = Register.objects.filter(username=u,password=p).exists()

	result = ""
	request.session['logged_in'] = valid_user
	if valid_user:
		return render(request,"adhome.html",{})
	else:
		result = "Wrong password"
		return render(request,"admin.html",{ 'result' : result})
#1. courier details
def hello(request):
	if 'logged_in' in request.session and request.session['logged_in']==True:
		all_data=courier_d.objects.all()
		print all_data
		return render(request,"courierd.html",{'data':all_data})
	else:
		return render(request,"admin.html")

#2. user details -signup

def bush(request):
	if 'logged_in' in request.session and request.session['logged_in']==True:
		all_data=bushire.objects.all()
		print all_data
		return render(request,"abushire.html",{'data':all_data})
	else:
		return render(request,"admin.html")

def seat(request):
	return render(request,"seats.html")

