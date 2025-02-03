import pytest
from PasswordValidator import check_password_strength,EXP_CHAR_MSG,EXP_DGT_MSG,EXP_LWRL_MSG,EXP_MSL_MSG,EXP_SPLCHAR_MSG,EXP_UPPR_MSG,SCS_PASSWORD_STRNG

def test_password_char():
    assert check_password_strength("Short1!") == (False,EXP_CHAR_MSG)

def test_password_dgt():
    assert check_password_strength("DIgitNO!@!") == (False,EXP_DGT_MSG)

def test_password_lwrCse():
    assert check_password_strength("UPPERCASEONLY") == (False,EXP_LWRL_MSG)

def test_password_UpprCse():
    assert check_password_strength("alllowercase&5") == (False,EXP_UPPR_MSG)

def test_password_Spcl_charIssue():
    assert check_password_strength("t7HiPAh4iL") == (False,EXP_SPLCHAR_MSG)

#def test_password_GenericIssue():
#    assert check_password_strength("t7Hi PAh4iL") == (False,EXP_MSL_MSG)

def test_password_valid():
    assert check_password_strength("t7Hi#PAh4iL") == (True,SCS_PASSWORD_STRNG)
    assert check_password_strength("PasswrD!2%") == (True,SCS_PASSWORD_STRNG)