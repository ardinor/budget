﻿Budget
================================

The early stages of a budgeting site writing with Django.

**NB.** Development is taking placing in Python 3, not currently tested under Python 2.

TO DO
-------------------------
- Think of a better name.
- Add balance transfers, e.g., when you transfer money to savings, automatically create a credit on your savings account when the debit on the transaction account is made.
- Add recurring debits/transactions? Maybe add a check, to say you've ensured that transaction took place for that amount e.g., you actually received your salary of $xxx.xx and you didn't get $yyy.yy which would throw out the calculations.

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
    python manage.py sqlmigrate budget xxxx
    python manage.py migrate
