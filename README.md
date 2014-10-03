Budget
================================

The early stages of a budgeting site writing with Django.

**NB**./ Development is taking placing in Python 3, not currently tested under Python 2.

TO DO
-------------------------
- Think of a better name.
- Add balance transfers, e.g., when you transfer money to savings, automatically create a credit on your savings account when the debit on the transaction account is made.

REQUIREMENTS
-------------------------

Python

See requirements.txt

TO USE
-------------------------
Create superuser

    python manage.py createsuperuser

MISC
-------------------------
If model changes are made (in the budget app for example):

    python manage.py makemigrations budget
    python manage.py migrate
