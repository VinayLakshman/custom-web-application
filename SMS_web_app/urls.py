from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login_user,name='login page'),

    path('logistics_home',views.logistics_page,name='Logistics Page'),
    path('receive_module_logistic_details',views.ReceiveModuleLogisticDetails,name='Receive Module- Logistic Details'),
    path('receive_module_unit_details',views.ReceiveModuleUnitDetails,name='Receive Module- Unit Details'),

    path('admin_home',views.admin_page,name='Admin Page'),
    path('Add_Account',views.AdminModuleAddAccount,name='Admin Module- Add Account'),
    path('Password_Reset',views.AdminModulePasswordReset,name='Admin Module- Password Reset'),

    path('logout_user',views.logout_user,name='logout user'),
    path('user_profile',views.user_profile,name='user profile'),

    path("password_reset", views.password_reset_request, name="password_reset")
    ]