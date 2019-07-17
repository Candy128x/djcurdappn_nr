from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validate user entered password correct or not
        if password1 == password2:
            print('Password not matching..!')

        # Validate user username
        elif User.objects.filter(username=user_name).exists():
            print('User name already exist. Enter unique user name, Try again!')

        # Validate user eMail
        elif User.objects.filter(email=email).exists():
            print('Email ID already exist. Enter unique Email ID, Try again!')

        # Save user data
        else:
            user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=first_name,
                                            last_name=last_name)
            user.save()
            print('User Created')

        return redirect('/accounts/register')

    else:
        return render(request, 'register.html')
