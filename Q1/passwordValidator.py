import re,sys

EIGHT_CHARACTER_EXP="Password must be at least 8 characters long."
LOWER_CASE_EXP="Password must contain at least one lowercase letter."
UPPER_CASE_EXP="Password must contain at least one uppercase letter."
DIGIT_CASE_EXP="Password must contain at least one digit."
SPECIALCHAR_CASE_EXP="Password must contain at least one special character (!@#$%)."
REGEX_VALID="Password is Valid"
REGEX_INVAlID_EXP=EIGHT_CHARACTER_EXP+'\n'+LOWER_CASE_EXP+'\n'+UPPER_CASE_EXP+'\n'+DIGIT_CASE_EXP+'\n'+SPECIALCHAR_CASE_EXP

def check_password_strength (password):

    if len(password) < 8:
        return False, EIGHT_CHARACTER_EXP
    if not re.search(r"[a-z]", password):
        return False, LOWER_CASE_EXP
    if not re.search(r"[A-Z]", password):
        return False, UPPER_CASE_EXP
    if not re.search(r"[0-9]", password):
        return False, DIGIT_CASE_EXP
    if not re.search(r"[!@#\$%]", password):
        return False, SPECIALCHAR_CASE_EXP
    try:
        regex = r"^(\S)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%])(?=.*\d)[a-zA-Z0-9!@#$%]{8,}$"
        match = re.match(regex, password)
        if match:
            return True, REGEX_VALID
        else:
            return False, REGEX_INVAlID_EXP
    except Exception as ex :
            return False, f"\nAn unexpected error occurred: {ex}"
            print(f"\nAn unexpected error occurred: {ex}")
        
    #return True, "Password is Valid"

if __name__ == '__main__':

    #password = input("Enter your password")
    #is_strong, message = check_password_strength(password)
    #print(message)

    #this section belongs to provide password without interruption
    try:
        while True:
            password = input("Enter your password (or Ctrl+C to exit): ")
            is_strong, message = check_password_strength(password)
            print(message)
            if is_strong :
                print(message)
                break
            else:
                print("\nPlease try again...")
    except KeyboardInterrupt:
        print("\nPassword input interrupted. Exiting.")
        sys.exit(0) # exit the program 