from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request,'index.html',{})

def sign_in_view(request):
    return render(request,'account-sign-in-cover.html',{})

def sign_up_view(request):
    return render(request,'account-sign-up-cover.html',{})

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

