import pytest
from passwordValidator import check_password_strength

EIGHT_CHARACTER_EXP="Password must be at least 8 characters long."
LOWER_CASE_EXP="Password must contain at least one lowercase letter."
UPPER_CASE_EXP="Password must contain at least one uppercase letter."
DIGIT_CASE_EXP="Password must contain at least one digit."
SPECIALCHAR_CASE_EXP="Password must contain at least one special character (!@#$%)."
REGEX_VALID="Password is Valid"
REGEX_INVAlID_EXP=EIGHT_CHARACTER_EXP+'\n'+LOWER_CASE_EXP+'\n'+UPPER_CASE_EXP+'\n'+DIGIT_CASE_EXP+'\n'+SPECIALCHAR_CASE_EXP

def test_validPassword():
    assert check_password_strength("PasswrD!2") == (True,REGEX_VALID)

def test_invalidPasswithSpace():
    assert check_password_strength("t7Hi# PAh4iL") == (False,REGEX_INVAlID_EXP)
    
