import random
import cv2

def verification():
   varification = cv2.VideoCapture(0)
   while True:
       ret,frame=varification.read()
       cv2.imshow('verification',frame)
       if ret:
          if cv2.waitKey(20) & 0xFF == ord('1'):
             break
   varification.release()
   cv2.destroyAllWindows()

def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == "exit":
            print("Exit successful")
            exit()
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input <= 10:
                return user_input
            else:
                print("Error: Input must be between 0 and 10. Try again.")
        else:
            print("Invalid input. Please enter a number between 0 and 10, or type 'EXIT' to quit.")


def generate_strong_password():
    # verification()
    
    cp_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    sm_char = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    symbol = ['@', '!', '~', '$', '>', '<', '/', '?']
    number = ['1', '2', '3', '4', '5', '6', '7', '8']
    
    print('"Sir"\nPlease make sure your input is not above 10 numbers\n')
    
    num_cp_char = get_valid_input('Choose how many "Capital Letters" you need OR enter "EXIT":\n')
    num_sm_char = get_valid_input('Choose how many "Small Letters" you need OR enter "EXIT":\n')
    num_symbol = get_valid_input('Choose how many "Symbols" you need OR enter "EXIT":\n')
    num_number = get_valid_input('Choose how many "Numbers" you need OR enter "EXIT":\n')
    
    password = []
    
    for ps_w in range(num_cp_char):
        password.append(random.choice(cp_char))
    for ps_w  in range(num_sm_char):
        password.append(random.choice(sm_char))
    for ps_w in range(num_symbol):
        password.append(random.choice(symbol))
    for ps_w in range(num_number):
        password.append(random.choice(number))
    
    random.shuffle(password)
    print(password)
    
    passwords = ""
    for psw in password:
        passwords+=psw
    print(passwords)


generate_strong_password()
