from rest_framework import serializers
from .models import Restaurant, Menu


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name']

    def create(self, validated_data):
        name = validated_data.pop('name', None)
        instance = self.Meta.model(**validated_data)
        if name is not None:
            instance.name = name
            instance.save()
            return instance
        return None


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'price', 'menu', 'day', 'restaurant']

    def create(self, validated_data):
        menu = Menu.objects.filter(restaurant_id=validated_data["restaurant"].id, day=int(validated_data["day"]))
        if len(menu) == 0:
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
        else:
            menu = menu.first()
            menu.menu = validated_data["menu"]
            menu.price = validated_data["price"]
            menu.save()
            return menu
