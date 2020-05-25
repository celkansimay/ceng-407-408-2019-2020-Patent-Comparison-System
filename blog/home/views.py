from django.shortcuts import render
import pymongo 
# Create your views here.

def home_view(request):
    return render(request,'index.html',{})

def sign_in_view(request):
    return render(request,'account-sign-in-cover.html',{})

def sign_up_view(request):
	if 'email' in request.GET: 
	
		print ("---------SIGN UP REQUEST RECEIVED-----------");
		print ("reading values from GET request...")
		email     = request.GET['email']
		password  = request.GET['pass']
		print("received values from GET request are...");
		print(" -email :   ", email)
		print(" -pass  :   ", password)
		print("calling insert values...")
		insertAccount(email, password)
		print("values are successfully inserted to db")
		print ("----------SIGNUP REQUEST PROCESSED-----------");
	return render(request,'account-sign-up-cover.html',{})

def insertAccount(email, password):
	client = pymongo.MongoClient("mongodb://localhost:27017/")
	#Database name: testdb
	db = client["patent"]
	#collection name : accounts
	collection = db["accounts"]
	#query 
	query = {"email": email, "pass": password}
	#execute query
	collection.insert_one(query)

def forgot_password_view(request):
    return render(request,'account-forgot-password.html',{})

def patent_one_view(request):
    return render(request,'patent-1.html',{})

def patent_second_view(request):
    return render(request,'patent-2.html',{})

def patent_third_view(request):
    return render(request,'patent-3.html',{})

def patent_fourth_view(request):
    return render(request,'patent-4.html',{})

def patent_fifth_view(request):
    return render(request,'patent-5.html',{})    

def contact_view(request):
    return render(request,'contact.html',{})    

def who_we_are_view(request):
    return render(request,'who_we_are.html',{}) 

def our_vision_view(request):
    return render(request,'our_vision.html',{})   

def result_view(request):
    return render(request,'result.html',{})          

def submit(request):
	print ("---------SUBMIT REQUEST RECEIVED-----------");
	print ("reading values from GET request...")
	name   = request.GET['name']
	email  = request.GET['email']
	title  = request.GET['title']
	desc   = request.GET['desc']
	claim  = request.GET['claim']
	ipc    = request.GET['ipc']
	sector = request.GET['sector']
	print("received values from GET request are...");
	print(" -name:   ", name)
	print(" -email:  ", email)
	print(" -title:  ", title)
	print(" -desc:   ", desc)
	print(" -claim:  ", claim)
	print(" -ipc:    ", ipc)
	print(" -sector: ", sector)
	print("calling insert values...")
	insertPatent(name, email, title, desc, claim, ipc, sector)
	print("values are successfully inserted to db")
	print ("----------SUBMIT REQUEST PROCESSED-----------");
	return render(request, 'submit.html', {})
	
	
	
def insertPatent(name, email, title, desc, claim, ipc, sector):
	
	client = pymongo.MongoClient("mongodb://localhost:27017/")
	#Database name: testdb
	db = client["patent"]
	#collection name : patent
	collection = db["patent"]
	#query 
	query = { "name": name, "email": email, "title": title, "desc": desc, "claim":claim, "ipc":ipc, "sector":sector }
	#execute query
	collection.insert_one(query)

def controlUser(email,password):
		
	client = pymongo.MongoClient("mongodb://localhost:27017/")
	db = client["patent"]
	collection = db["accounts"]
	query = {"email":email, "password":password}
	collection.find(query)



