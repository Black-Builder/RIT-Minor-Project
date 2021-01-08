from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth 
from .models import signupform, loginform, Importantlink
# Create your views here.

def home(request):
    return render(request, 'core/index.html')
    # return HttpResponse('hello')

def base(request):
    return render(request, 'core/base.html')

def aboutpage(request):
    return render(request, 'core/about.html')    

def admissionspage(request):
    return render(request, 'core/admission.html')    

def coursespage(request):
    return render(request, 'core/courses.html')

def feepage(request):
    return render(request, 'core/fee.html')


def facultypage(request):
    return render(request, 'core/faculty.html')    



def gallerypage(request):
    return render(request, 'core/gallery.html')    

def formspage(request):
    return render(request, 'core/forms.html')

# View for signup form
def signuppage(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Email = request.POST['Email']
        Password1 = request.POST['Password']
        Password2 = request.POST['Password2']
        print('User filled the form')
        if Password1 == Password2:
            if User.objects.filter(email=Email).exists():
                messages.info(request,'Email already taken')
                if User.objects.filter(username=Username).exists():
                  messages.info(request,'Username already taken')
                return redirect('signup')    
            else:
                user = User.objects.create_user(username=Username, password=Password2, email=Email, first_name=Firstname, last_name=Lastname)
                user.save()
                return render(request,"accounts/login.html")
                print('A new user created')
        else:
            messages.info(request,'password not matching')
            print('password not matching')  
            return render(request, "accounts/signup.html")  
    else:
        print('User Opened Signup Form')
        form = signupform()
        return render(request, 'accounts/signup.html', {'form':form})

# View for login form    
def loginpage(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"accounts/login.html")
        else:
            return render(request,"accounts/signup.html")         
    else:
        return render(request, 'accounts/login.html')  

def logout(request):
    auth.logout(request)
    return render(request,"core/index.html") 

def important_link(request):
    links = Importantlink()
    return render(request, 'core/fee.html', {'links':links})    