from django.urls import path
from .views import CustumerUserCreateView,CustumerUserListeView,CustumerUserDetailView,CustumerUserUpdateView, CustumerUserDeleteView,Update_staff,Update_admin,Update_etat,CustumerUserProfile,UpdateCustumerUserProfile,UpdatePassword,changes_password
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import views

app_name = 'accounts'

urlpatterns = [
    path('create/',login_required(CustumerUserCreateView.as_view()),name="create"),
    path('',login_required(CustumerUserListeView.as_view()),name="index"),
    path('update_staff/',login_required(Update_staff), name='update_staff'),
    path('update_admin/',login_required(Update_admin), name='update_admin'),
    path('update_etat/',login_required(Update_etat), name='update_etat'),
    path('detail/<str:slug>/',login_required(CustumerUserDetailView.as_view()), name='detail'),
    path('edit/<str:slug>/',login_required(CustumerUserUpdateView.as_view()),name="update"),
    path('delete/<str:slug>/',login_required(CustumerUserDeleteView.as_view()), name="delete"),
    path('mon_profile/',login_required(CustumerUserProfile.as_view()), name="mon_profile"),
    path('profile/<str:slug>/',login_required(UpdateCustumerUserProfile.as_view()),name='update_profile'),
    path('update_password/',login_required(UpdatePassword.as_view()),name='update_password'),
    path('changer_password/',login_required(changes_password),name='changer_password'),
    
     # ------------------------------PASSWORD RESET--------------------------------
    path('reset_password/', views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),name="password_reset"),
    path('reset_password_send/', views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),name="password_reset_done"),
    path('reset_password_confirm/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),name="password_reset_complete"),
]

