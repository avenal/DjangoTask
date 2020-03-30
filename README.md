# DjangoTask
How to install
- git clone this repo
- cd into cloned folder
- create virtualenv && pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- navigate to localhost:8000/

Finished:
1. Set up a basic (latest or LTS) Django installation
2. Extend the User model to have a birthday field of type date and a random number field of type integer that is assigned a value from 1-100 on creation
3. Views for: list of all users, viewing, adding, editing and deleting a single user
4. Create two template tags: a tag that will display "allowed" if the user is > 13 years old otherwise display "blocked" and a tag that will display the BizzFuzz result of the random number that was generated
for the user.
5. Add a column to the list view after the birthday column that uses the allowed/blocked tag
6. Optional task

Not finished:
1. Unit test what you feel is apropriate to test
