import datetime

from rest_framework.response import Response
from .serializers import RestaurantSerializer, MenuSerializer
from .models import *
from rest_framework.views import APIView


class RestaurantView(APIView):
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CreateMenuView(APIView):
    def post(self, request, restaurant_id):
        data = request.data
        data.update({"restaurant": restaurant_id})
        serializer = MenuSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ShowRestaurantWeekMenuView(APIView):
    def get(self, request, restaurant_id):
        restaurant_week_menu = Menu.objects.filter(restaurant_id=restaurant_id).order_by('day').values()
        return Response(restaurant_week_menu)


class showAllCurrentDayMenuView(APIView):
    def get(self, request, day_id):
        day_menus = Menu.objects.filter(day=day_id).order_by('day', 'restaurant_id').values()
        return Response(day_menus)


class showCurrentDayVotesResult(APIView):
    def get(self, request):
        today_day = datetime.datetime.today().weekday()
        most_voted_menu = Menu.objects.filter(day=today_day).order_by('-votes')[0]
        if most_voted_menu.votes > 0:
            return Response(
                f"Today most voted meny is: {most_voted_menu}. (Menu ID: {most_voted_menu.id}, Menu votes: {most_voted_menu.votes})"
            )
        return Response("Nobody has voted for the menu yet today :(")

