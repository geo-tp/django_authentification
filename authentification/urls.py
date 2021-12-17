
from django.urls import path, include
from allauth.account.views import confirm_email
from django.conf.urls import url

urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
    path('accounts-rest/registration/account-confirm-email/<key>', confirm_email, name='account_confirm_email'),
]