def display_invoice(username, amount, due_date):
    print(f"hello{ username}")
    print(f" your bill of ${amount:.2f} is due : {due_date}")
    
display_invoice("sid", 10, "01/05/2025")

