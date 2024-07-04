
def complex_calculation(num):
    try:
        result = num/(num-5)
        print(f"{result}")
    except Exception as e:
        print("an error occured")
        
try:
    user_input = float(input("enter the number"))
except:
    print("please enter an integer or float")
else:
    complex_calculation(user_input) #this else block prevents printing the op even if wrong
