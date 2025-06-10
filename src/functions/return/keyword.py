#keyword arguments = an argument preceded by an identifier
#                    helps with readibility
#                    order of an argements dosen't matter


def hello(greetings, title, first, last):
    print(f"{greetings}  {title}{first} {last}")

hello(greetings = "Hello", title="Mr.", last="sid" , first= " the kid")