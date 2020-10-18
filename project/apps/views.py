from django.shortcuts import render,redirect,HttpResponse
from .models import Contact
from django.contrib import messages
import smtplib as s


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    
    if request.method=="POST":
       fname=request.POST.get('fname','')
       lname=request.POST.get('lname','')
       email=request.POST.get('email','')
       password=request.POST.get('password','')
       phoneno=request.POST.get('phoneno','')
       
        # validation
       value = {
            'fname': fname,
            'lname': lname,
            'phoneno': phoneno,
            'email': email
        }
       error_message = None

       contact = Contact(fname=fname,
                            lname=lname,
                            phoneno=phoneno,
                            email=email,
                            password=password)
       if (not contact.fname):
            error_message = "First Name Required !!"
       elif len(contact.fname) < 4:
            error_message = 'First Name must be 4 char long or more'
       elif not contact.lname:
            error_message = 'Last Name Required'
       elif len(contact.lname) < 4:
            error_message = 'Last Name must be 4 char long or more'
       elif not contact.phoneno:
            error_message = 'Phone Number required'
       elif len(contact.phoneno) < 10:
            error_message = 'Phone Number must be 10 char Long'
       elif not contact.password:
            error_message = 'Password required'
       elif len(contact.password) < 6:
            error_message = 'Password must be 6 char long'
       elif not contact.email:
            error_message = 'Email required'
       elif len(contact.email) < 5:
            error_message = 'Email must be 5 char long'
       elif contact.isExists():
            error_message = 'Email address is already registered'
       if not error_message:
            contact.save()           
            messages.success(request, 'Account has created successfully')
            ob=s.SMTP("smtp.gmail.com",587)
            ob.starttls()
            ob.login("vssarika18@gmail.com","Sowbhar@n1")
            subject="Account Activation of the mail"
            body="Your account has been activated successfully.Thank you for the registration.For any additional queries,contact this number 6382584890"
            message="Subject:{}\n\n{}".format(subject,body)
            ob.sendmail("vssarika18@gmail.com",email,message)
            ob.quit()
            return render(request,'index.html',{'fname':fname})

       else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'index.html', data)

    return render(request,'index.html')
