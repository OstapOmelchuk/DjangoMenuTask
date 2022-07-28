from django.db import models

DAYS_OF_WEEK = [
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
]


class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    price = models.FloatField(default=0)
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=0)
    menu = models.TextField(blank=False, default='')
    votes = models.IntegerField(default=0)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.restaurant.name} | {DAYS_OF_WEEK[self.day][1]} MENU"
