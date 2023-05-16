# if/else  $$  try/except

def give_me_num(num):
    if num > 0:
        print(f"Your number {num} is positive")
    elif num == 0:
        print(f"Your number is {num}")
    #if we use isdigit() then we don't need to check is the number is negative 
    # else:   
    #     print(f"Your number {num} is negative")

def validate_input():
    try:    
        if user_input.isdigit():
            user_num = int(user_input)  
            give_me_num(user_num)
             
    except ValueError:
        print("This is not a valid number, please stop it!")

user_input = input("User, give me a number and I can tell you if is positive!\n")

validate_input()
  
    
