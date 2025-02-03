import re
import sys  # Import the sys module

EXP_CHAR_MSG= "Password must be at least 8 characters long."
EXP_LWRL_MSG="Password must contain at least one lowercase letter."
EXP_UPPR_MSG="Password must contain at least one uppercase letter."
EXP_DGT_MSG="Password must contain at least one digit."
EXP_SPLCHAR_MSG="Password must contain at least one special character (!@#$%)."
EXP_MSL_MSG=EXP_CHAR_MSG+"\n"+EXP_LWRL_MSG+"\n"+EXP_UPPR_MSG+"\n"+EXP_DGT_MSG+"\n"+EXP_SPLCHAR_MSG

SCS_PASSWORD_STRNG="Password is strong."


def check_password_strength(password):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%])(?=.*\d)[a-zA-Z0-9!@#$%]{8,}$"

    if len(password) < 8:
        return False,EXP_CHAR_MSG

    if not re.search(r"[a-z]", password):
        return False,EXP_LWRL_MSG

    if not re.search(r"[A-Z]", password):
        return False,EXP_UPPR_MSG

    if not re.search(r"[0-9]", password):
        return False,EXP_DGT_MSG

    if not re.search(r"[!@#\$%]", password):
        return False,EXP_SPLCHAR_MSG
    
    #to capture other password validate case
    if re.search(regex,password) == None:
        return False,EXP_MSL_MSG
    
    return True, SCS_PASSWORD_STRNG
        

if __name__ == '__main__':
    try:
        while True:
            password = input("Enter your password (or Ctrl+C to exit): ")
            result = check_password_strength(password)
            
            if result:  # if result is not None
              is_strong, message = result
              print(message)

              if is_strong:
                  break
              else:
                  print("Please try again...")
            else:
              print("Unexpected Error")

    except KeyboardInterrupt:
        print("\nPassword input interrupted. Exiting.")
        sys.exit(0) # Gracefully exit the program