import datetime
import jwt
from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from myapp.models import Menu
from myapp.serializers import MenuSerializer
from .models import User
from .serializers import UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


def get_user_by_token(request):
    token = request.COOKIES.get('jwt')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    return serializer.data


class UserView(APIView):
    def get(self, request):
        data = get_user_by_token(request)
        return Response(data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class VoteForMenuView(APIView):
    def post(self, request, menu_id):
        user_data = get_user_by_token(request)
        today_day = datetime.datetime.today().weekday()

        menu = Menu.objects.get(pk=menu_id)
        if today_day != menu.day:
            return Response("This menu is not for current day.")
        user = User.objects.get(pk=user_data["id"])

        if not user.vote_for:
            user.vote_for = menu_id
            menu.votes += 1
            user.save()
            menu.save()
            return Response(f"User Vote For Menu With ID={user.vote_for} Menu Votes: {menu.votes}")
        elif int(user.vote_for) != int(menu_id):
            msg = ""
            if user.vote_for:
                early_voted_meny = Menu.objects.get(pk=user.vote_for)
                early_voted_meny.votes -= 1
                early_voted_meny.save()
                msg = f" Deleted 1 Vote from Menu With ID={early_voted_meny.id} => Menu Votes (-1): {early_voted_meny.votes}"
            user.vote_for = menu_id
            menu.votes += 1

            user.save()
            menu.save()

            return Response(f"User Vote For Menu With ID={user.vote_for} Menu Votes (+1): {menu.votes} ..................." + msg)
        return Response("You already voted for this menu!")


def index(request):
    return render(request, "auth/home.html")
