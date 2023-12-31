from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user, logout

def registration(request):

    if request.method == 'POST':

        firstName = request.POST.get('f_name')
        lastName = request.POST.get('l_name')
        userName = request.POST.get('u_name')
        email  = request.POST.get('email')
        pass_1 = request.POST.get('pass_1')
        pass_2 = request.POST.get('pass_2')

        if pass_1 != pass_2:
            return render(request,'admin/register.html')
        else:
            user_reg = User.objects.create_user(userName,email,pass_1)
            # user_reg.is_active = False
            user_reg.first_name = firstName
            user_reg.last_name = lastName
            user_reg.email = email
            
            user_reg.save()
            return redirect('login')

            

            # user_reg = User(

            #     first_name = firstName,
            #     last_name  = lastName,
            #     username   = userName,
            #     email  =     email,
            #     password =   pass_1,
            # #     # is_active = False

            # )
            # user_reg.save()
            # return redirect('login')
            



    return render(request,'admin/register.html')


# def loginUser(request):
#     if request.method == "POST":

#         u_name = request.POST.get('userName')
#         psw  = request.POST.get('password')
#         user = authenticate(usename=u_name, password=psw )
#         # print(u_name)
#         # print(psw)
#         # print(user)
#         # if user is not None:
#         #     if User.is_active !=0 and User.is_superuser:
#         #         login(request,user)
#         #     return redirect('dashboard')
#         if user is not None:
#             print(u_name)
#             print(psw)
#             # if User.is_active !=0 and User.is_superuser:
#             #     login(request,user)
#             # return redirect('dashboard')
#             login_user(request, user)
#             return redirect('dashboard')
    
#     return render(request,'admin/login.html')

def loginUser(request):
    if request.method == "POST":
        u_name = request.POST.get('userName')
        psw = request.POST.get('password')
        
        user = authenticate(username = u_name, password = psw)
        

        if user is not None:
            if User.is_active !=0 and User.is_superuser:
                login_user(request,user)
            return redirect('dashboard')

    return render(request,'admin/login.html')




def logoutUser(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'admin/dashboard.html')
    else:
        return redirect('login')
