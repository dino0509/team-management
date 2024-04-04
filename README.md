# Basic web app for team management using Django

## To start

In the project directory, you can run:

### `python manage.py migrate` to create the database tables based on the defined models
### `python manage.py runserver` to run application server.

You can then navigate to `http://127.0.0.1:8000/member_management` in your web browser to visit the app.

## Overview

To keep it simple, I decided to use the default SQLite3 database. I added basic validation rules on the Name, email and phone fields. 
The name fields only support upper and lower case alphabets and the phone number only supports numbers. Phone number can also be empty.
I used the `validate_email` method available in the Django core library for email validation.
