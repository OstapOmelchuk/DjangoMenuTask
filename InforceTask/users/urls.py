from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, index, VoteForMenuView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('vote/<int:menu_id>/', VoteForMenuView.as_view()),
    path('', index)
]
