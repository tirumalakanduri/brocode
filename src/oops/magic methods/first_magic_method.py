#magic methods = dunder methods (double underscore)  1__init__ , __str__ , __eq__
#                they are automatically called by many of python's built in operationns.
#                they allow developers to define or cutomize the behavior of objects.



class book:
    

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    

    def __eq__(self, other):
         return self.title == other.title and self.author == other.author
book1 = book("the hobbit", "j.j.r tolkien", 310)
book2 = book("harry potter", " j,k rolling", 223)
book3 = book("the lion , the witch , the wardrobe", " c.s. lewis", 1732)



print(book1)

print(book1 == book2)