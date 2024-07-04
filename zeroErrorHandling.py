# Exercise 1: Handling ZeroDivisionError
num = int(input("enter the numerator"))
den = int(input("enter the denominator"))

def safe_division(num,den):
    try:
        b= num/den
        return b
    except ZeroDivisionError:
        print("the number you provided is zero")
        return None
    except:
        print("Other than zero division error")
print(safe_division(num,den))