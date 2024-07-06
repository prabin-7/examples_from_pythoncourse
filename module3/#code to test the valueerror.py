#code to test the valueerror5
import math 
def sqrt_num():
    try:
        num = float(input("enter the number to calc sqrt")) # int tells the input is integer
        s = math.sqrt(num)
        return s
    except ValueError:
        print('Value error: please enter integer or float')
        return None
    # except:
    #     print("please enter valid intger or float")
print(sqrt_num())