from django.urls import path
from .views import RestaurantView, CreateMenuView, ShowRestaurantWeekMenuView, showAllCurrentDayMenuView, \
    showCurrentDayVotesResult

urlpatterns = [
    path("", RestaurantView.as_view()),
    path("restaurant/<int:restaurant_id>/week_menu/", ShowRestaurantWeekMenuView.as_view()),
    path("restaurant/<int:restaurant_id>/", CreateMenuView.as_view()),
    path("restaurant/day/<int:day_id>/", showAllCurrentDayMenuView.as_view()),
    path("todays-menu/", showCurrentDayVotesResult.as_view())
]
