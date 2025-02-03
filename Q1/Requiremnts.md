# Python Exercise

## Question 1 

Q1. In DevOps, security is a crucial aspect, and ensuring strong passwords is essential. Create a Python script to check the strength of the password. 

●       Implement a Python function called check_password_strength that takes a password string as input.

●       The function should check the password against the following criteria:

○       Minimum length: The password should be at least 8 characters long.

○       Contains both uppercase and lowercase letters.

○       Contains at least one digit (0-9).

○       Contains at least one special character (e.g., !, @, #, $, %).

●       The function should return a boolean value indicating whether the password meets the criteria.

●       Write a script that takes user input for a password and calls the check_password_strength function to validate it.

●       Provide appropriate feedback to the user based on the strength of the password.  

## Test results-pytest

```
python -m pytest .\Test_passwordValidator.py
====================================================== test session starts ======================================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Devops\CodeBase\githubrepo\HRViredPy\Q1
collected 5 items

Test_passwordValidator.py .....                                                                                            [100%]

======================================================= 5 passed in 0.18s ======================================================= 

```
## Test results-console 

```
Enter your password (or Ctrl+C to exit): sHort1!
Password must be at least 8 characters long.
Please try again...
Enter your password (or Ctrl+C to exit): uppercases
Password must contain at least one uppercase letter.
Please try again...
Enter your password (or Ctrl+C to exit): LOWERCASES
Password must contain at least one lowercase letter.
Please try again...
Enter your password (or Ctrl+C to exit): P@@ssW~rd@25
Password is strong.
```