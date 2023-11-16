from django.urls import path
from users.views import login, registration, profile, logout, usercompanyadd_u


app_name = 'users'

urlpatterns = [
    path('', login, name='login_p'),
    path('registration/', registration, name='registration_p'),
    path('profile/', profile, name='profile_p'),
    path('logout/', logout, name='logout_p'),
    path('companyadd/<int:company_id>/', usercompanyadd_u, name='usercompanyadd_u'),
]
