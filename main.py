# print("Crash Course")
# variables and data type
cal_to_units = 24
unit = "hours"

# print(f"20 days are {20*cal_to_units} {unit}")
# print(f"35 days are {35*cal_to_units} {unit}")
# print(f"50 days are {50*cal_to_units} {unit}")
# print(f"110 days are {110*cal_to_units} {unit}")

# function *def*

def days_to_units():
    print(f"20 days are {20 * cal_to_units} {unit}")
    print("All set")    

# days_to_units()

def days_with_params(num_of_days):
    print(f"{num_of_days} days are {num_of_days * cal_to_units} {unit}")
    print("Now with params")

# days_with_params(10)

# scope 
def scope(num_of_days):
    print(num_of_days) #this variable is not the same as the function days_with_params
    print(unit)

scope(1)