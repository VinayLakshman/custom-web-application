from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class EmployeeID:
    def __init__(self,email):
        self.email=email

    def generate_emp_id(self):
        emp= User.objects.filter(email=self.email).first()
        if emp is not None:
            str_id=str(emp.id).zfill(5)
            emp_id=f'C-{str_id}'
            return emp_id

department=[('','-'),('admin','Admin'),('logistic','Logistic')]
# creating a form
class LoginForm(forms.Form):
    email = forms.CharField(max_length=200,widget=forms.EmailInput,label='Email ID')
    password = forms.CharField(widget=forms.PasswordInput(),label='Password')
    department=forms.CharField(widget=forms.Select(choices=department),label='Department')

#class AdminForm(forms.Form):
  #  add_ename=forms.CharField(min_length=5,max_length=50,label='Employee Name',required=False)
  #  add_email = forms.CharField(max_length=200, widget=forms.EmailInput, label='Employee Email ID',required=False)
   # add_department = forms.CharField(widget=forms.Select(choices=department), label='Employee Department',required=False)

class PasswordUpdateForm(forms.Form):
    emp_email=forms.CharField(widget=forms.EmailInput(),label='Employee Email ID')
    password=forms.CharField(widget=forms.PasswordInput(),label="New Password")

class AdminForm(UserCreationForm):
    email = forms.CharField(max_length=200, widget=forms.EmailInput(), label='Employee Email ID')
    department = forms.CharField(widget=forms.Select(choices=department), label='Employee Department')

    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)
        for fieldname in ['email','department','password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['email','department']


class UpdatePassword(forms.Form):
    newpassword=forms.CharField(widget=forms.PasswordInput, label='Enter New Password', required=True)


class ReceiveModuleLogisticDetailsForm(forms.ModelForm):
    c_choices=[('','-')]
    cust=Customer.objects.all()
    for x in cust:
        c_choices.append(tuple([f'{x.Name}-{x.Circle}',f'{x.Name}-{x.Circle}']))
    Customer_Name=forms.CharField(widget=forms.Select(choices=c_choices))
    Received_From = forms.CharField(max_length=222)
    Number_Of_Boxes = forms.IntegerField()
    DC_Date=forms.CharField(max_length=50,required=False)

    class Meta():
        fields= "__all__"
        model = LogisticDetail


class ReceiveModuleUnitDetailsForm(forms.ModelForm):
    class Meta():
        fields='__all__'
        model=UnitDetail
