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