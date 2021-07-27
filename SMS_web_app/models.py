
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    empid=models.CharField(_('Employee ID'),unique=False,max_length=10,default='',null=True)
    department=models.CharField(_('Employee Department'),unique=False,max_length=20,default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class LogisticDetail(models.Model):
    Person_Name = models.CharField(max_length=100,default='null')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    Contact_Number = models.CharField(validators=[phone_regex], max_length=17, default='null')  # validators should be a list
    Courier_Name = models.CharField(max_length=100, default='null')
    Tracking_ID = models.CharField(max_length=100, default='null')
    DC_Number = models.IntegerField(unique=True)
    Received_From = models.CharField(max_length=40)
    Number_Of_Boxes = models.IntegerField()
    DC_Date = models.CharField(max_length=50,default='')
    # No_of_Units = models.IntegerField(default='1')
    CHOICES = [('','-'),('y', 'Yes'), ('n', 'No')]
    without_document = models.CharField(choices=CHOICES,max_length=128,default='')
    WD_comments = models.CharField(max_length=100,default='')
    Damage_Shipment = models.CharField(choices=CHOICES, max_length=128, default='')
    DS_comments = models.CharField(max_length=100, default='')
    Short_or_Excess_Shipment = models.CharField(choices=CHOICES, max_length=128, default='')
    SE_comments = models.CharField(max_length=100, default='')
    Unit_Value=models.CharField(choices=CHOICES,max_length=128,default='')
    Currency_Format=models.CharField(max_length=100, default='')


class UnitDetail(models.Model):
    Serial_Number = models.CharField(max_length=123,unique=True)
    Part_Number = models.CharField(max_length=123)
    Description = models.TextField(max_length=322)
    Word_Order_Number = models.CharField(max_length=345)
    With_Accessories_Choice = models.CharField(choices=[('','-'),('y','Yes'),('n','No')],max_length=134)
    Number_Of_Accessories = models.IntegerField()
    Repeat_Repair_Choice = models.CharField(choices=[('','-'),('y',"Yes"),('n',"No")],max_length=134)
    Repeat_Repair_Comment = models.TextField(max_length=123)

class Customer(models.Model):
    Name=models.CharField(max_length=100)
    Circle=models.CharField(max_length=100)
