from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user  = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')    
# Create your views here.
def register(request):
    
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already taken.. try other username')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already taken.. try other email')
                return redirect('register')

            else:      
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = first_name,last_name = last_name )
                user.save();
                return redirect('login')
        else:
           messages.info(request,'password not matching..')
           return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')