from django.urls import path
from users.views import login, registration, profile, logout

app_name = 'users'

urlpatterns = [
    path('', login, name='login_p'),
    path('registration/', registration, name='registration_p'),
    path('profile/', profile, name='profile_p'),
    path('logout/', logout, name='logout_p'),
]
