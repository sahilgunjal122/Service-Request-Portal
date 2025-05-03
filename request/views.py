from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,user_passes_test

from .models import ServiceRequest
from .forms import ServiceRequestForm

from django.core.mail import send_mail

# Create your views here.

@login_required
def index_page(request):
    return render(request,'index.html')

def login_page(request):
    if request.method== "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            error_message="Invalid credentials"
            return render(request,'login.html',{'error_message':error_message})

    return render(request,'login.html')

def sign_page(request):
    if request.method =="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repeatPassword=request.POST['repeatPassword']

        if password==repeatPassword:
            try:
                user=User.objects.create_user(username,email,password)
                user.save()
                login(request,user)
                return redirect('/')
            except:
                error_message="Error Creating the User"
                return render(request,'signup.html',{'error_message':error_message})

        else:
            error_message="Password Does not match"
            return render(request,'signup.html',{'error_message':error_message})



    return render(request,'signup.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def request_submit(request):
    #This is just an acknowlgement Page
    return render(request,'request_submitted.html')

@login_required
def submit_request(request):
    if request.method =="POST":
        form=ServiceRequestForm(request.POST,request.FILES)
        if form.is_valid():
            service_request=form.save(commit=False)
            service_request.user=request.user
            service_request.save()
            return redirect('/request_submitted')
    else:
        form=ServiceRequestForm()
    return render(request,'submit_request.html',{'form':form})
        
@login_required
def request_list(request):
    requests=ServiceRequest.objects.filter(user=request.user).order_by('submitted_at')
    return render(request,'request_list.html',{'requests':requests})


def is_admin(user):
    return user.is_staff

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    requests=ServiceRequest.objects.all().order_by('submitted_at')
    return render(request,'admin_dashboard.html',{'requests':requests})

def update_request_status(request,pk):
     service_request = get_object_or_404(ServiceRequest, pk=pk)

     if request.method == 'POST':
        new_status = request.POST.get('status')
        request_obj = get_object_or_404(ServiceRequest, pk=pk)
        request_obj.status = new_status
        request_obj.save()
     
    # Send Email Notification
        send_mail(
            subject='Service Request Status Updated',
            message=f"Dear {service_request.user.username},\n\n"
                    f"We would like to inform you that the status of your service request titled "
                    f"'{service_request.title}' has been updated to: '{new_status}'.\n\n"
                    f"If you have any questions or require further assistance, please don't hesitate to reach out to our support team.\n\n"
                    f"Thank you for using our services.\n\n"
                    f"Best regards,\n"
                    f"The Gas Utility Service Team",
            from_email='sahilgunjal122476@gmail.com',
            recipient_list=[service_request.user.email],
        )
        return redirect('admin_dashboard')


