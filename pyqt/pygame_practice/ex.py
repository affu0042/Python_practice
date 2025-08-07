try:
    num = int(input("Enter a number"))
    res = 10/num
except ValueError:
    print("Enter a valid value")
except ZeroDivisionError:
    print("cannot divide by zero")
else:
    print(f"The Result is {res}")
finally:
    print("finally block always get executed")