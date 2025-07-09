#class methods =  Allow operations related to the class itself.
#                 takes (cls) as the first parameter , which represents the class itself.



class student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.total_gpa =+ gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"
    

    @classmethod
    def get_count(cls):
        return f"total no of students : {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"


student1 = student("sid", 3.2)
student2 = student("kid", 3.4)
student3 = student("did", 3.5)
print(student.get_count())
print(student.get_average_gpa())