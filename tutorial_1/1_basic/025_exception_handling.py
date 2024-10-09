# exception =   events detected during execution that interrupt the flow of the program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number divide by: "))
    
except ZeroDivisionError as e:
    print(e)
    print("you can't divide by zero!")
except ValueError as e:
    print(e)
    print("enter only numbers please")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    result = numerator / denominator
    print(result)
finally:
    print("this will always execute")


# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number divide eeeeeeby: "))
# except ZeroDivisionError as e:
#     print(e)
#     print("You cannot divide by zero! idiot")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers please")
# except Exception as e:
#     print(e)
#     print("something went wrong")
# else:
#     result = numerator / denominator
#     print(result)
# finally:
#     print("this will always execute")
