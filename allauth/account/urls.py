from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path("signup/", views.signup, name="account_signup"),
    path("verify_email/<uidb64>/<password>", views.verify_email, name="verify_email"),
    path('verification-success/', TemplateView.as_view(template_name="account/verification_success.html"), name='verification_success'),
    path('verification-error/', TemplateView.as_view(template_name="account/verification_error.html"), name='verification_error'),
    path('sigup_reponse/', TemplateView.as_view(template_name="account/sigup_reponse.html"), name='sigup_reponse'),
    
    
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path("reauthenticate/", views.reauthenticate, name="account_reauthenticate"),
    path(
        "password/change/",
        views.password_change,
        name="account_change_password",
    ),
    path("password/set/", views.password_set, name="account_set_password"),
    path("inactive/", views.account_inactive, name="account_inactive"),
    # Email
    path("email/", views.email, name="account_email"),
    # path(
    #     "confirm-email/",
    #     views.email_verification_sent,
    #     name="account_email_verification_sent",
    # ),
    # re_path(
    #     r"^confirm-email/(?P<key>[-:\w]+)/$",
    #     views.confirm_email,
    #     name="account_confirm_email",
    # ),
    # password reset
    path("password/reset/", views.password_reset, name="account_reset_password"),
    path(
        "password/reset/done/",
        views.password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        views.password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "password/reset/key/done/",
        views.password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
]
