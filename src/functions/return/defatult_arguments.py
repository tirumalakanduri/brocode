#default arguments = A default value for certain parameters
#                     default is used when that argument is omitted 
#                     make your functions more flexible, reduces # for argements


def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))

