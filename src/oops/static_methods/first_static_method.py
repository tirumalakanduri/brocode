#Static methods = A method that belong to a class rather than any object from that class(instance)
#                 usually used for general utility function

#instance methods = best for operations on instance of the class(ojects)
#Static methods = Best for utility functions that do not need access to class data


class employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "janitor"]
        return position in valid_positions


employee1 = employee("sid", "Manager")
employee2 = employee("kid", "Cashier")
employee3 = employee("did", "cook")

print(employee.is_valid_position("Cook"))  # Output: True



print(employee1.get_info())