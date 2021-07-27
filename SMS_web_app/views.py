from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils.encoding import force_bytes
from django.conf import settings
from .forms import *
from django.contrib import messages
from .models import *
from django import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm


def login_user(request):
    login_form=LoginForm()
    if request.method=='POST':
        if 'loginaccount' in request.POST:
            login_form=LoginForm(request.POST)
            if login_form.is_valid():
                emp = authenticate(username=login_form.cleaned_data['email'], password=login_form.cleaned_data['password'])
                if emp is not None:
                    login(request, emp)
                    emp = User.objects.filter(email=request.POST['email']).first()
                    if emp is not None:
                        emp_dep = emp.department
                    dep = request.POST['department']
                    if dep == emp_dep:
                        if dep == 'admin':
                            return redirect('Admin Page')
                        elif dep == 'logistic':
                            return redirect('Logistics Page')
                    else:
                        messages.error(request, 'Entered department was found to be incorrect')
                        return render(request, 'login/login_page.html', {'form': login_form})
                else:
                    messages.error(request,'Invalid Login Credentials')
                    return render(request,'login/login_page.html',{'form':LoginForm(request.POST)})
    return render(request,'login/login_page.html',{'form':login_form})
# Create your views here.

@login_required()
def logout_user(request):
    if request.method=='POST':
        logout(request)
        messages.success(request,'User has been logged out')
        return redirect('login page')

@login_required()
def user_profile(request):
    updtpass=UpdatePassword()
    if request.method=="POST":
        if 'updatepass' in request.POST:
            updtpass=UpdatePassword(request.POST)
            if updtpass.is_valid():
                new_password=request.POST['newpassword']
                emp=User.objects.get(email=request.user.email)
                emp.set_password(new_password)
                emp.save()
                messages.success(request,"Password updated successfully!")
            return render(request,'login/userprofile.html',{'updatepassword':updtpass})
    return render(request, 'login/userprofile.html', {'updatepassword': updtpass})

@login_required()
def logistics_page(request):
    return render(request, 'home/logistic_home.html')


@login_required()
def admin_page(request):
    return render(request,'home/admin_home.html')

@login_required()
def AdminModuleAddAccount(request):
    cemp_id = ''
    admin_form = AdminForm()
    admin_form.fields['password1'].widget = forms.HiddenInput()
    admin_form.fields["password1"].initial = "dcba54321"
    admin_form.fields['password2'].widget = forms.HiddenInput()
    admin_form.fields["password2"].initial = "dcba54321"
    if request.method == 'POST':
        admin_form = AdminForm(request.POST)
        admin_form.fields['password1'].widget = forms.HiddenInput()
        admin_form.fields['password2'].widget = forms.HiddenInput()
        admin_form.fields["password1"].initial = "dcba54321"
        admin_form.fields["password2"].initial = "dcba54321"
        if admin_form.is_valid():
            emp_email = admin_form.cleaned_data['email']
            admin_form.save()
            emp_id = EmployeeID(emp_email)
            cemp_id = emp_id.generate_emp_id()
            emp = User.objects.get(email=emp_email)
            emp.set_password(cemp_id)
            emp.save()
            emp.empid = cemp_id
            emp.save(update_fields=['empid'])
            return render(request, 'Admin module/add_account.html',
                          {'adminform': admin_form, 'emp_id': cemp_id})
    return render(request,'Admin module/add_account.html',{'adminform':admin_form})

@login_required()
def AdminModulePasswordReset(request):
    prform=PasswordUpdateForm()
    if request.method == 'POST':
        prform = PasswordUpdateForm(request.POST)
        if prform.is_valid():
            pwd_emp_email = prform.cleaned_data['emp_email']
            pwd_new_password = prform.cleaned_data['password']
            try:
                pwd_emp = User.objects.get(email=pwd_emp_email)
            except:
                pwd_emp = None
                messages.error(request, 'Entered email address did not match with any existing employees')
            if pwd_emp != None:
                pwd_emp.set_password(pwd_new_password)
                pwd_emp.save()
                messages.success(request,'Password Updated Successfully!')
            return render(request, 'Admin module/password_reset.html',
                          {'pass_reset_form': prform})
    return render(request, 'Admin module/password_reset.html', {'pass_reset_form': prform})




def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            user = User.objects.filter(email=data).first()
            if user is not None:
                    subject = "Password Reset Requested"
                    email_template_name = "password/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'SMS Plus',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'A message with instructions to reset the password has been sent to your inbox.')
                    return redirect("login page")
        messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


def ReceiveModuleLogisticDetails(request):
    logistic_form = ReceiveModuleLogisticDetailsForm()
    if request.method=="POST":
        logistic_form=ReceiveModuleLogisticDetailsForm(request.POST)
        logistic_form.fields['DC_Date'].initial='null'
        if logistic_form.is_valid():
            p_name=logistic_form.cleaned_data.get('Person_Name')
            con_no=logistic_form.cleaned_data.get('Contact_Number')
            c_name=logistic_form.cleaned_data.get('Courier_Name')
            c_id=logistic_form.cleaned_data.get('Tracking_ID')
            if p_name != 'null' and con_no != 'null' and c_name!= 'null' and c_id != 'null':
                messages.error(request,"Cannot submit both 'by hand' and 'by courier' fields, please select any one")
                return redirect('Receive Module- Logistic Details')
            date=request.POST.get('DCDate')
            logistic_form.save()
            ldf=LogisticDetail.objects.get(DC_Number=logistic_form.cleaned_data.get("DC_Number"))
            ldf.DC_Date=date
            ldf.save()
            messages.success(request,'Entered Logistic Details were updated successfully')
            return redirect('Receive Module- Logistic Details')
        else:
            messages.error(request,'Something went wrong, check for errors and try again')
    return render(request,'Receive module/logistic_details.html',{'form':logistic_form})

@login_required()
def ReceiveModuleUnitDetails(request):
    unit_form=ReceiveModuleUnitDetailsForm()
    if request.method=='POST':
        unit_form=ReceiveModuleUnitDetailsForm(request.POST)
        if unit_form.is_valid():
            unit_form.save()
            messages.success(request,'Entered Unit Details were updated Successfully')
            return redirect('Receive Module- Unit Details')
        else:
            messages.error(request, 'Something went wrong, check for errors and try again')
    return render(request,'Receive module/unit_details.html',{'form':unit_form})
