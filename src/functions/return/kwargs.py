#kwargs = it allows you to pass multiple keyword arguments 
#         it collects into a dictionary

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_address(street =  "123 john street",
                          city = "stratford",
                          state = "CT",
                          zip = " 06614")


print("--------------------------------------")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ") 
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')}  {kwargs.get('zip')}")

print()


shipping_label("Dr.", "sid", "the kid","iii" ,
               street =  "123 john street",
               pobox = "pobox # 1001",
               apt = "100",
               city = "stratford",
               state = "CT",
               zip = " 06614")




