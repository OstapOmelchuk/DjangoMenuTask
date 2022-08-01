# Change directory to source folder ()

    cd <path to this project>/InforceTask/
___
# Environment variables

in source directory (<path to this project>/InforceTask/) create .env file and add:

    POSTGRES_HOST='localhost'

    POSTGRES_DB='MenuApp'

    POSTGRES_USER='postgres'

    POSTGRES_PASSWORD='ftQazWsxc321'

<br>

___
# Installation of necessary packages


To install all the packages activate your virtualenv and run the following command in your terminal:
    
    pip install -r requirements.txt

<br>

---
# Creating a database

To create DB - type in your terminal:

    createdb -h <your_postgres_host> -p <your_postgres_port> -U <your_username> MenuApp

for example:

    createdb -h localhost -p 5432 -U postgres MenuApp

To create a table in your DB just run a run.py file and the table automatically will be created if it did not exist

<br>

___

# Migrations

Type in your terminal:

    python manage.py makemigrations

then:
    
    python manage.py migrate


# Start app

    python manage.py runserver

.

___

# Endpoints to check in Postman:

___
.

### register user: 

    method POST: http://127.0.0.1:8000/register/
    
### body.raw.JSON :

        {
            "username": "Test1",
            "email": "test1@gmail.com",
            "password": "test1password" 
        }
---
### login user

    method POST: http://127.0.0.1:8000/login/

### body.raw.JSON :

        {
            "email": "test1@gmail.com",
            "password": "test1password"
        }

___

### check if authorised

    method GET: http://127.0.0.1:8000/user/
 ___
### Logout

    method POST: http://127.0.0.1:8000/logout/
___
### Vote for menu (only when you are logged in)

    method POST: http://127.0.0.1:8000/vote/<int: id_of_menu>/

Can vote form menus from different restaurants but only for current day
___

### Create restaurant

    method POST: http://127.0.0.1:8000/api/

### body.raw.JSON:

    {
        "name": "TestRestaurantName"
    }
___

### show menu for each day (if menus have been added to the restaurant)

    method GET: http://127.0.0.1:8000/api/restaurant/<int: id_of_restaurant>/week_menu/
___

### Add menu to particular restaurant 

If the menu of the selected restaurant for the specified day already exists - it will be overwritten, i.e. updated to the one you specify)

    method POST: http://127.0.0.1:8000/api/restaurant/10/

### body.raw.JSON:

    {
        "price": 10.5,
        "menu": "Menu for day 3 (Thursday)",
        "day": 3
    }
___
### Show all menus from all restaurants for current day

    method GET: http://127.0.0.1:8000/api/restaurant/day/<int: day_id>/

day_id - from 0 to 6 

    0 - Monday,
    2 - Tuesday,
    ... ,
    ... ,
    6 - Sunday

___
### Get the menu of the day (with max votes for current day)

    method GET: http://127.0.0.1:8000/api/todays-menu/
