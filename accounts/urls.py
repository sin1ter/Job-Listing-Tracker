from django.urls import path
from .views import SignUpView, ProfileView, EditProfileView, CustomLoginView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),

]
