#exception = An Event that interupts the flow of progrom)
#            (ZeroDivisionError,   typeerror,    ValueError)
#            1. try     ,    2. except,       3.finally
 


try:
    number = int(input("enter the number: "))
    print(1/number)
except ZeroDivisionError:
    print("you can't divide by zero!")
except ValueError:
    print("enter only number please !")
except Exception:
    print("something went wrong!")
finally:
    print("Do some cleanup here")