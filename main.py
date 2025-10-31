# Library Management System

#imports
import tkinter as tk

#OBJECTIVES
'''

1. Book database
2. User database
3. Issue/Return books
4. Admin and User roles
5. Search functionality
6. Inventory management

'''



# book management interface
def BOOK_MGMT_INTERFACE(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Book Management", font=("Times Roman", 20))
    label.pack(pady=40)

    ADD_BTN = tk.Button(root, text="Add Book", font=("Times Roman", 14), command=lambda: add_book_interface(root))
    ADD_BTN.pack(pady=10)
    DEL_BTN = tk.Button(root, text=" Remove Book", font=("Times Roman", 14), command=lambda: delete_book_interface(root))
    DEL_BTN.pack(pady=10)
    BACK_BTN = tk.Button(root, text="Back to Main Menu", font=("Times Roman", 14), command=lambda: main_interface(root))
    BACK_BTN.pack(pady=10)

def add_book_interface(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Add New Book", font=("Times Roman", 16))
    label.pack(pady=20)
    name_label = tk.Label(root, text="Book Name:", font=("Times Roman", 14))
    name_label.place(x=20, y=100)
    name_entry = tk.Entry(root, font=("Times Roman", 14))
    name_entry.place(x=220, y=100)

    author_label = tk.Label(root, text="Author Name:", font=("Times Roman", 14))
    author_label.place(x= 20, y=150)
    author_entry = tk.Entry(root, font=("Times Roman", 14))
    author_entry.place(x=220, y=150)

    copies_label = tk.Label(root, text="Number of Copies:", font=("Times Roman", 14))
    copies_label.place(x=20, y=200)
    copies_entry = tk.Entry(root, font=("Times Roman", 14))
    copies_entry.place(x=220, y=200)

    add_btn = tk.Button(root, text="Add", font=("Times Roman", 14), command=lambda: add_book(name_entry.get(), author_entry.get(), copies_entry.get()))
    add_btn.place(x=150, y=250)
    
    back_btn = tk.Button(root, text="Back", font=("Times Roman", 14), command=lambda: BOOK_MGMT_INTERFACE(root))
    back_btn.place(x=250, y=250)

def add_book(name, author, copies):
    name, author, copies = name.strip(), author.strip(), copies.strip()
    if copies.isdigit() and int(copies) > 0:
        
        with open("books.txt", "r") as book_db_file:
            
            book_db = book_db_file.readlines()

        if [name, author] in (book.split("||")[0:2] for book in book_db):
            appendScrn = tk.Tk()
            appendScrn.title("Error")
            appendScrn.geometry("")
            label = tk.Label(appendScrn, text=f"This book already exists in the database. Add {copies} more copies to database?", font=("Times Roman", 12))
            label.pack(pady=20)

            def append_copies():
                for i in range(len(book_db)):
                    book_name, author_name, available_copies = book_db[i].strip().split("||")
                    if book_name.lower() == name.lower() and author_name.lower() == author.lower():
                        new_copies = int(available_copies) + int(copies)
                        book_db[i] = f"{book_name}||{author_name}||{new_copies}\n"
                        break
                with open("books.txt", "w") as book_db_file:
                    book_db_file.writelines(book_db)
                appendScrn.destroy()
            yes_btn = tk.Button(appendScrn, text="Yes", font=("Times Roman", 12), command=append_copies)
            yes_btn.pack(side=tk.RIGHT, padx=100, pady=5)
            cancel_btn = tk.Button(appendScrn, text="Cancel", font=("Times Roman", 12), command=appendScrn.destroy)
            cancel_btn.pack(side=tk.LEFT, padx=100, pady=5)
            
            appendScrn.mainloop()
            return
        
        else:
            with open("books.txt", "a") as book_db_file:
                book_db_file.write(f"{name}||{author}||{copies}\n")

            addedScrn = tk.Tk()
            addedScrn.title("Book Added")
            addedScrn.geometry("")
            label = tk.Label(addedScrn, text=f"Book '{name}' by {author} with {copies} copies added successfully!", font=("Times Roman", 12))
            label.pack(pady=40)
            ok_btn = tk.Button(addedScrn, text="OK", font=("Times Roman", 12), command=addedScrn.destroy)
            ok_btn.pack(pady=10)
            addedScrn.mainloop()
    else:
        errorScrn = tk.Tk()
        errorScrn.title("Error")
        errorScrn.geometry("")
        label = tk.Label(errorScrn, text="Please enter a valid number of copies.", font=("Times Roman", 12))
        label.pack(pady=40)
        ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=errorScrn.destroy)
        ok_btn.pack(pady=10)
        errorScrn.mainloop()

def delete_book_interface(root):
    
    for widget in root.winfo_children():
        widget.destroy()


    label = tk.Label(root, text="Remove Book", font=("Times Roman", 16))
    label.pack(pady=20)
    
    name_label = tk.Label(root, text="Book Name:", font=("Times Roman", 14))
    name_label.place(x=20, y=80)
    name_entry = tk.Entry(root, font=("Times Roman", 14))
    name_entry.place(x=220, y=80)
    
    author_label = tk.Label(root, text="Author Name:", font=("Times Roman", 14))
    author_label.place(x=20, y=125)
    author_entry = tk.Entry(root, font=("Times Roman", 14))
    author_entry.place(x=220, y=125)
    
    copies_label = tk.Label(root, text="No. of copies to delete:", font=("Times Roman", 14))
    copies_label.place(x=20, y=170)
    copies_entry = tk.Entry(root, font=("Times Roman", 14), width=5)
    copies_entry.place(x=250, y=170)

    book_label = tk.Label(root, text="Book Name:", font=("Times Roman", 14))
    book_label.place(x=20, y=200)
    book_list = tk.Listbox(root, font=("Times Roman", 12), width=30)

    author_name_label = tk.Label(root, text="Author Name:", font=("Times Roman", 14))
    author_name_label.place(x=300, y=200)
    author_list = tk.Listbox(root, font=("Times Roman", 12), width=20)

    copies_count_label = tk.Label(root, text="Copies:", font=("Times Roman", 10))
    copies_count_label.place(x=500, y=200)
    copies_list = tk.Listbox(root, font=("Times Roman", 12), width=5)

    book_list.place(x=20, y=220)
    author_list.place(x=300, y=220)
    copies_list.place(x=500, y=220)

    scrollbar = tk.Scrollbar(root, command=lambda *args: (book_list.yview(*args), author_list.yview(*args), copies_list.yview(*args)))
    scrollbar.place(x=555, y=221, height=201)

    book_list.config(yscrollcommand=scrollbar.set)
    author_list.config(yscrollcommand=scrollbar.set)
    copies_list.config(yscrollcommand=scrollbar.set)

    del_btn = tk.Button(root, text="Delete", font=("Times Roman", 14), command=lambda: delete_book(root, name_entry.get(), author_entry.get(), copies_entry.get()))
    del_btn.place(x=150, y=440)

    back_btn = tk.Button(root, text="Back", font=("Times Roman", 14), command=lambda: BOOK_MGMT_INTERFACE(root))
    back_btn.place(x=250, y=440)

    book_list.bind("<<ListboxSelect>>", lambda event: select(book_list, author_list, name_entry, author_entry))
    
    with open("books.txt", "r") as book_db_file:
        book_list_data = book_db_file.readlines()
        for book in book_list_data:
            book_name, author_name, copies = book.strip().split("||")
            book_list.insert(tk.END, book_name)
            author_list.insert(tk.END, author_name)
            copies_list.insert(tk.END, copies)

    name_entry.bind("<KeyRelease>", lambda event: update_book_list(name_entry, author_entry, book_list, author_list, copies_list))
    author_entry.bind("<KeyRelease>", lambda event: update_book_list(name_entry, author_entry, book_list, author_list, copies_list))

def select(lst1, lst2, entry1, entry2):
    
    indices = lst1.curselection()

    if not indices:
        return
    selected_index = indices[0]

    
    selected_book, selected_author = lst1.get(selected_index), lst2.get(selected_index)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.insert(0, selected_book)
    entry2.insert(0, selected_author)

def update_book_list(name_entry, author_entry, book_list, author_list, copies_list):
    book_list.delete(0, tk.END)
    author_list.delete(0, tk.END)
    copies_list.delete(0, tk.END)
    with open("books.txt", "r") as book_db_file:
        book_list_data = book_db_file.readlines()
        for book in book_list_data:
            book_name, author_name, copies = book.strip().split("||")
            if name_entry.get().strip().lower() in book_name.lower() and author_entry.get().strip().lower() in author_name.lower():
                book_list.insert(tk.END, book_name)
                author_list.insert(tk.END, author_name)
                copies_list.insert(tk.END, copies)

def delete_book(root, name, author, copies):

    name, author, copies = name.strip().lower(), author.strip().lower(), copies.strip()
    if not copies.isdigit() or int(copies) <= 0:
        errorScrn = tk.Tk()
        errorScrn.title("Error")
        errorScrn.geometry("")
        label = tk.Label(errorScrn, text="Please enter a valid number of copies to delete.", font=("Times Roman", 12))
        label.pack(pady=40)
        ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=errorScrn.destroy)
        ok_btn.pack(pady=10)
        errorScrn.mainloop()
        return

    with open("books.txt", "r") as book_db_file:
        book_db = book_db_file.readlines()

    for book in book_db:
        book_name, author_name, available_copies = book.strip().split("||")
        if book_name.lower() == name.lower() and author_name.lower() == author.lower():
            if int(available_copies) >= int(copies):
                new_copies = int(available_copies) - int(copies)
                if new_copies > 0:
                    book_db[book_db.index(book)] = f"{book_name}||{author_name}||{new_copies}\n"
                else:
                    book_db.pop(book_db.index(book))
                with open("books.txt", "w") as book_db_file:
                    book_db_file.writelines(book_db)

                deletedScrn = tk.Toplevel(root)
                deletedScrn.title("Book Deleted")
                deletedScrn.geometry("")
                label = tk.Label(deletedScrn, text=f"Deleted {copies} copies of '{name}' by {author}.", font=("Times Roman", 12))
                label.pack(pady=40)
                ok_btn = tk.Button(deletedScrn, text="OK", font=("Times Roman", 12), command=lambda: (deletedScrn.destroy, delete_book_interface(root)))
                ok_btn.pack(pady=10)
                deletedScrn.mainloop()
                return
            
            else:
                errorScrn = tk.Tk()
                errorScrn.title("Error")
                errorScrn.geometry("")
                label = tk.Label(errorScrn, text="Not enough copies available to delete.", font=("Times Roman", 12))
                label.pack(pady=40)
                ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=errorScrn.destroy)
                ok_btn.pack(pady=10)
                errorScrn.mainloop()
                return  


# user management interface
def USER_MGMT_INTERFACE(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="User Management", font=("Times Roman", 20))
    label.pack(pady=40)

    ADD_BTN = tk.Button(root, text="Add User", font=("Times Roman", 14), command=lambda: add_user_interface(root))
    ADD_BTN.pack(pady=10)
    DEL_BTN = tk.Button(root, text=" Remove User", font=("Times Roman", 14), command=lambda: remove_user_interface(root))
    DEL_BTN.pack(pady=10)
    BACK_BTN = tk.Button(root, text="Back to Main Menu", font=("Times Roman", 14), command=lambda: main_interface(root))
    BACK_BTN.pack(pady=10)

def add_user_interface(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Add New User", font=("Times Roman", 16))
    label.pack(pady=20)
    username_label = tk.Label(root, text="Username:", font=("Times Roman", 14))
    username_label.place(x=20, y=100)
    username_entry = tk.Entry(root, font=("Times Roman", 14))
    username_entry.place(x=220, y=100)

    phone_label = tk.Label(root, text="Phone No.:", font=("Times Roman", 14))
    phone_label.place(x= 20, y=150)
    phone_entry = tk.Entry(root, font=("Times Roman", 14))
    phone_entry.place(x=220, y=150)

    adress_label = tk.Label(root, text="Adress:", font=("Times Roman", 14))
    adress_label.place(x=20, y=200)
    adress_entry = tk.Entry(root, font=("Times Roman", 14))
    adress_entry.place(x=220, y=200)

    add_btn = tk.Button(root, text="Add", font=("Times Roman", 14), command=lambda: add_user(username_entry.get(), phone_entry.get(), adress_entry.get()))
    add_btn.place(x=150, y=250)
    
    back_btn = tk.Button(root, text="Back", font=("Times Roman", 14), command=lambda: USER_MGMT_INTERFACE(root))
    back_btn.place(x=250, y=250)

def add_user(username, phone, adress):
    username, phone, adress = username.strip(), phone.strip(), adress.strip()
    if phone.isdigit() and len(phone) == 10:
        
        with open("users.txt", "r") as user_db_file:
            user_db = user_db_file.readlines()

        if phone in (user.split("||")[1] for user in user_db):
            errorScrn = tk.Tk()
            errorScrn.title("User Exists")
            errorScrn.geometry("")
            
            label = tk.Label(errorScrn, text=f"A user already exists in the database with the given phone number. Please use another number.", font=("Times Roman", 12))
            label.pack(pady=20)

            ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=errorScrn.destroy)
            ok_btn.pack(pady=10)
            errorScrn.mainloop()
            return
        
        else:
            with open("users.txt", "a") as user_db_file:
                user_db_file.write(f"{username}||{phone}||{adress}\n")

            addedScrn = tk.Tk()
            addedScrn.title("Book Added")
            addedScrn.geometry("")
            label = tk.Label(addedScrn, text=f"User '{username}' has been registered on the phone number {phone} successfully!", font=("Times Roman", 12))
            label.pack(pady=40)
            ok_btn = tk.Button(addedScrn, text="OK", font=("Times Roman", 12), command=addedScrn.destroy)
            ok_btn.pack(pady=10)
            addedScrn.mainloop()
    else:
        errorScrn = tk.Tk()
        errorScrn.title("Error")
        errorScrn.geometry("")
        label = tk.Label(errorScrn, text="Please enter a valid phone number.", font=("Times Roman", 12))
        label.pack(pady=40)
        ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=errorScrn.destroy)
        ok_btn.pack(pady=10)
        errorScrn.mainloop()

def remove_user_interface(root):
    for widget in root.winfo_children():
        widget.destroy()


    label = tk.Label(root, text="Remove User", font=("Times Roman", 16))
    label.pack(pady=20)
    
    username_label = tk.Label(root, text="Username:", font=("Times Roman", 14))
    username_label.place(x=20, y=80)
    username_entry = tk.Entry(root, font=("Times Roman", 14))
    username_entry.place(x=220, y=80)
    
    phone_label = tk.Label(root, text="Phone No.:", font=("Times Roman", 14))
    phone_label.place(x=20, y=125)
    phone_entry = tk.Entry(root, font=("Times Roman", 14))
    phone_entry.place(x=220, y=125)

    user_label = tk.Label(root, text="Book Name:", font=("Times Roman", 14))
    user_label.place(x=20, y=200)
    username_list = tk.Listbox(root, font=("Times Roman", 12), width=30)

    phone_label = tk.Label(root, text="Phone:", font=("Times Roman", 14))
    phone_label.place(x=300, y=200)
    phone_list = tk.Listbox(root, font=("Times Roman", 12), width=10)

    adress_label = tk.Label(root, text="Adress:", font=("Times Roman", 14))
    adress_label.place(x=400, y=200)
    adress_list = tk.Listbox(root, font=("Times Roman", 12), width=15)

    username_list.place(x=20, y=220)
    phone_list.place(x=300, y=220)
    adress_list.place(x=400, y=220)

    scrollbar = tk.Scrollbar(root, command=lambda *args: (username_list.yview(*args), phone_list.yview(*args), adress_list.yview(*args)))
    scrollbar.place(x=555, y=221, height=201)

    username_list.config(yscrollcommand=scrollbar.set)
    phone_list.config(yscrollcommand=scrollbar.set)
    adress_list.config(yscrollcommand=scrollbar.set)

    del_btn = tk.Button(root, text="Remove", font=("Times Roman", 14), command=lambda: remove_user(root, username_entry.get(), phone_entry.get()))
    del_btn.place(x=150, y=440)

    back_btn = tk.Button(root, text="Back", font=("Times Roman", 14), command=lambda: USER_MGMT_INTERFACE(root))
    back_btn.place(x=350, y=440)

    username_list.bind("<<ListboxSelect>>", lambda event: select(username_list, phone_list, username_entry, phone_entry))
    
    with open("users.txt", "r") as user_db_file:
        user_list_data = user_db_file.readlines()
        for user in user_list_data:
            user_name, phone_number, user_adress = user.strip().split("||")
            username_list.insert(tk.END, user_name)
            phone_list.insert(tk.END, phone_number)
            adress_list.insert(tk.END, user_adress)

    username_entry.bind("<KeyRelease>", lambda event: update_user_list(username_entry, phone_entry, username_list, phone_list, adress_list))
    phone_entry.bind("<KeyRelease>", lambda event: update_user_list(username_entry, phone_entry, username_list, phone_list, adress_list))

def remove_user(root, username, phone):
    username, phone = username.strip(), phone.strip()

    with open("users.txt", "r") as user_db_file:
        user_db = user_db_file.readlines()

    for user in user_db:
        user_name, phone_number, user_adress = user.strip().split("||")
        if user_name == username and phone_number == phone:
            user_db.remove(user)
            with open("users.txt", "w") as user_db_file:
                user_db_file.writelines(user_db)

            removedScrn = tk.Toplevel(root)
            removedScrn.title("User Removed")
            removedScrn.geometry("")
            label = tk.Label(removedScrn, text=f"User '{username}' registered on the number {phone_number} has been removed successfully!", font=("Times Roman", 12))
            label.pack(pady=40)
            ok_btn = tk.Button(removedScrn, text="OK", font=("Times Roman", 12), command=lambda: (removedScrn.destroy, remove_user_interface(root)))
            ok_btn.pack(pady=10)
            removedScrn.mainloop()
            return

    errorScrn = tk.Tk()
    errorScrn.title("Error")
    errorScrn.geometry("")
    label = tk.Label(errorScrn, text="No matching user found.", font=("Times Roman", 12))
    label.pack(pady=40)
    ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=errorScrn.destroy)
    ok_btn.pack(pady=10)
    errorScrn.mainloop()

def update_user_list(username_entry, phone_entry, username_list, phone_list, adress_list):
    username_list.delete(0, tk.END)
    phone_list.delete(0, tk.END)
    adress_list.delete(0, tk.END)
    with open("users.txt", "r") as user_db_file:
        user_list_data = user_db_file.readlines()
        for user in user_list_data:
            user_name, phone_number, user_adress = user.strip().split("||")
            if username_entry.get().strip().lower() in user_name and phone_entry.get().strip().lower() in phone_number:
                username_list.insert(tk.END, user_name)
                phone_list.insert(tk.END, phone_number)
                adress_list.insert(tk.END, user_adress)


# issue/return interface
def ISSUE_RETURN_INTERFACE(root):   
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Issue/Return Books", font=("Times Roman", 20))
    label.pack(pady=40)

    ISSUE_BTN = tk.Button(root, text="Issue Book", font=("Times Roman", 14), command=lambda: issue_book_interface(root))
    ISSUE_BTN.pack(pady=10)

    RETURN_BTN = tk.Button(root, text=" Return Book", font=("Times Roman", 14), command=lambda: return_book_interface(root))
    RETURN_BTN.pack(pady=10)

    BACK_BTN = tk.Button(root, text="Back to Main Menu", font=("Times Roman", 14), command=lambda: main_interface(root))
    BACK_BTN.pack(pady=10)

def issue_book_interface(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Issue Book", font=("Times Roman", 16))
    label.pack(pady=20)

    phone_label = tk.Label(root, text="Phone No.:", font=("Times Roman", 14))
    phone_label.place(x=20, y=80)
    phone_entry = tk.Entry(root, font=("Times Roman", 14))
    phone_entry.place(x=220, y=80)

    book_name_label = tk.Label(root, text="Book Name:", font=("Times Roman", 14))
    book_name_label.place(x=20, y=125)
    book_name_entry = tk.Entry(root, font=("Times Roman", 14))
    book_name_entry.place(x=220, y=125)

    author_name_label = tk.Label(root, text="Author Name:", font=("Times Roman", 14))
    author_name_label.place(x=20, y=170)
    author_name_entry = tk.Entry(root, font=("Times Roman", 14))
    author_name_entry.place(x=220, y=170)

    issue_btn = tk.Button(root, text="Issue", font=("Times Roman", 14), command=lambda: issue_book(root, phone_entry.get(), book_name_entry.get(), author_name_entry.get()))
    issue_btn.place(x=20, y=250)

    back_btn = tk.Button(root, text="Back", font=("Times Roman", 14), command=lambda: ISSUE_RETURN_INTERFACE(root))
    back_btn.place(x=20, y=300)

    book_list = tk.Listbox(root, font=("Times Roman", 12), width=30)
    book_list.place(x=100, y=250)
    author_list = tk.Listbox(root, font=("Times Roman", 12), width=18)
    author_list.place(x=400, y=250)

    scrollbar = tk.Scrollbar(root, command=lambda *args: (book_list.yview(*args), author_list.yview(*args)))
    scrollbar.place(x=575, y=251, height=201)
    book_list.config(yscrollcommand=scrollbar.set)
    author_list.config(yscrollcommand=scrollbar.set)

    
    with open("books.txt", "r") as book_db_file:
        book_list_data = book_db_file.readlines()
        for book in book_list_data:
            book_name, author_name, copies = book.strip().split("||")
            book_list.insert(tk.END, book_name)
            author_list.insert(tk.END, author_name)


    book_name_entry.bind("<KeyRelease>", lambda event: update_issue_book_list(book_name_entry, author_name_entry, book_list, author_list))
    author_name_entry.bind("<KeyRelease>", lambda event: update_issue_book_list(book_name_entry, author_name_entry, book_list, author_list))
    book_list.bind("<<ListboxSelect>>", lambda event: select(book_list, author_list, book_name_entry, author_name_entry))

    
def update_issue_book_list(book_name_entry, author_name_entry, book_list, author_list):
    book_list.delete(0, tk.END)
    author_list.delete(0, tk.END)
    with open("books.txt", "r") as book_db_file:
        
        book_list_data = book_db_file.readlines()
        for book in book_list_data:
            book_name, author_name, copies = book.strip().split("||")
            if book_name_entry.get().strip().lower() in book_name.lower() and author_name_entry.get().strip().lower() in author_name.lower():
                book_list.insert(tk.END, book_name)
                author_list.insert(tk.END, author_name)

def issue_book(root, phone_num, book_name, author_name):
    with open("books.txt", 'r') as book_db_file:
        book_db = book_db_file.readlines()

    with open("users.txt", 'r') as user_db_file:
        user_db = user_db_file.readlines()
    
    with open("issues_db.txt", 'r') as issued_db_file:
        issued_db = issued_db_file.readlines()

    if phone_num not in (user.split("||")[1] for user in user_db):
        errorScrn = tk.Toplevel(root)
        errorScrn.title("Error")
        errorScrn.geometry("")
        label = tk.Label(errorScrn, text="No user found with the given phone number.", font=("Times Roman", 12))
        label.pack(pady=40)
        ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=lambda: (errorScrn.destroy, issue_book_interface(root)))
        ok_btn.pack(pady=10)
        errorScrn.mainloop()
        return
    
    for user in user_db:
        user_name, phone_number, user_adress = user.strip().split("||")
        if phone_num == phone_number:
            for book in book_db:
                book_n, author_n, copies = book.strip().split("||")
                if book_n == book_name and author_n == author_name:
                    if int(copies) > 0:
                        
                        issued_db.append(f"{phone_number}||{book_name}||{author_name}\n")
                        with open("issues_db.txt", 'w') as issued_db_file:
                            issued_db_file.writelines(issued_db)

                        new_copies = int(copies) - 1
                        book_db[book_db.index(book)] = f"{book_n}||{author_n}||{new_copies}\n"
                        with open("books.txt", 'w') as book_db_file:
                            book_db_file.writelines(book_db)
                        
                        return
                    else:
                        return

def return_book_interface(root):
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text="Return Book", font=("Times Roman", 16))
    label.pack(pady=20)

    phone_label = tk.Label(root, text="Phone No.:", font=("Times Roman", 14))
    phone_label.place(x=20, y=80)
    phone_entry = tk.Entry(root, font=("Times Roman", 14))
    phone_entry.place(x=220, y=80)

    book_name_label = tk.Label(root, text="Book Name:", font=("Times Roman", 14))
    book_name_label.place(x=20, y=125)
    book_name_entry = tk.Entry(root, font=("Times Roman", 14))
    book_name_entry.place(x=220, y=125)

    author_name_label = tk.Label(root, text="Author Name:", font=("Times Roman", 14))
    author_name_label.place(x=20, y=170)
    author_name_entry = tk.Entry(root, font=("Times Roman", 14))
    author_name_entry.place(x=220, y=170)

    return_btn = tk.Button(root, text="Return", font=("Times Roman", 14), command=lambda: return_book(root, phone_entry.get(), book_name_entry.get(), author_name_entry.get()))
    return_btn.place(x=20, y=250)

    back_btn = tk.Button(root, text="Back", font=("Times Roman", 14), command=lambda: ISSUE_RETURN_INTERFACE(root))
    back_btn.place(x=20, y=300)

    issues_list = tk.Listbox(root, font=("Times Roman", 12), width=30)
    issues_list.place(x=100, y=250)

    author_list = tk.Listbox(root, font=("Times Roman", 12), width=18)
    author_list.place(x=400, y=250)

    scrollbar = tk.Scrollbar(root, command=lambda *args: (issues_list.yview(*args), author_list.yview(*args)))
    scrollbar.place(x=575, y=251, height=201)
    issues_list.config(yscrollcommand=scrollbar.set)
    author_list.config(yscrollcommand=scrollbar.set)
    
    phone_entry.bind("<KeyRelease>", lambda event: update_return_book_list(phone_entry.get(), book_name_entry, author_name_entry, issues_list, author_list))
    author_name_entry.bind("<KeyRelease>", lambda event: update_return_book_list(phone_entry.get(), book_name_entry, author_name_entry, issues_list, author_list))
    book_name_entry.bind("<KeyRelease>", lambda event: update_return_book_list(phone_entry.get(), book_name_entry, author_name_entry, issues_list, author_list))
    issues_list.bind("<<ListboxSelect>>", lambda event: select(issues_list, author_list, book_name_entry, author_name_entry))

def update_return_book_list(phone_num, book_name_entry, author_name_entry, issues_list, author_list):
    issues_list.delete(0, tk.END)
    author_list.delete(0, tk.END)
    with open("issues_db.txt", "r") as issued_db_file:
        issued_list_data = issued_db_file.readlines()
        for issue in issued_list_data:
            issued_phone, issued_book, issued_author = issue.strip().split("||")
            if phone_num == issued_phone:
                if book_name_entry.get().strip().lower() in issued_book.lower() and author_name_entry.get().strip().lower() in issued_author.lower():
                    issues_list.insert(tk.END, issued_book)
                    author_list.insert(tk.END, issued_author)

def return_book(root, phone_num, book_name, author_name):
    with open("books.txt", 'r') as book_db_file:
        book_db = book_db_file.readlines()

    with open("issues_db.txt", 'r') as issued_db_file:
        issued_db = issued_db_file.readlines()

    with open("users.txt", 'r') as user_db_file:
        for user in user_db_file:
            user_name, phone_number, user_adress = user.strip().split("||")
            if phone_num == phone_number:
                break
        else:
            errorScrn = tk.Toplevel(root)
            errorScrn.title("Error")
            errorScrn.geometry("")
            label = tk.Label(errorScrn, text="No user found with the given phone number.", font=("Times Roman", 12))
            label.pack(pady=40)
            ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=lambda: (errorScrn.destroy, return_book_interface(root)))
            ok_btn.pack(pady=10)
            errorScrn.mainloop()
            return
        
    for issue in issued_db:
        issued_phone, issued_book, issued_author = issue.strip().split("||")
        if issued_phone == phone_num and issued_book == book_name and issued_author == author_name:
            issued_db.remove(issue)
            with open("issues_db.txt", 'w') as issued_db_file:
                issued_db_file.writelines(issued_db)

            for book in book_db:
                book_n, author_n, copies = book.strip().split("||")
                if book_n == book_name and author_n == author_name:
                    new_copies = int(copies) + 1
                    book_db[book_db.index(book)] = f"{book_n}||{author_n}||{new_copies}\n"
                    with open("books.txt", 'w') as book_db_file:
                        book_db_file.writelines(book_db)
                    
                    returnedScrn = tk.Toplevel(root)
                    returnedScrn.title("Book Returned")
                    returnedScrn.geometry("")
                    label = tk.Label(returnedScrn, text=f"Book '{book_name}' by {author_name} returned successfully!", font=("Times Roman", 12))
                    label.pack(pady=40)
                    ok_btn = tk.Button(returnedScrn, text="OK", font=("Times Roman", 12), command=lambda: (returnedScrn.destroy, return_book_interface(root)))
                    ok_btn.pack(pady=10)
                    return
                    

    errorScrn = tk.Toplevel(root)
    errorScrn.title("Error")
    errorScrn.geometry("")
    label = tk.Label(errorScrn, text="No matching issued book found for return.", font=("Times Roman", 12))
    label.pack(pady=40)
    ok_btn = tk.Button(errorScrn, text="OK", font=("Times Roman", 12), command=lambda: (errorScrn.destroy, return_book_interface(root)))
    ok_btn.pack(pady=10)
    errorScrn.mainloop()


def INVENTORY_INTERFACE(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    label = tk.Label(root, text="Library Inventory", font=("Times Roman", 20))
    label.pack(pady=20)

    book_entry_label = tk.Label(root, text="Book Name:", font=("Times Roman", 14))
    book_entry_label.place(x=20, y=80)
    book_entry = tk.Entry(root, font=("Times Roman", 14))
    book_entry.place(x=220, y=80)

    author_entry_label = tk.Label(root, text="Author Name:", font=("Times Roman", 14))
    author_entry_label.place(x=20, y=125)
    author_entry = tk.Entry(root, font=("Times Roman", 14))
    author_entry.place(x=220, y=125)

    book_list_label = tk.Label(root, text="Book Name", font=("Times Roman", 14))
    book_list_label.place(x=20, y=170)
    book_list = tk.Listbox(root, font=("Times Roman", 12), width=30)
    book_list.place(x=20, y=200)

    author_list_label = tk.Label(root, text="Author Name", font=("Times Roman", 14))
    author_list_label.place(x=320, y=170)
    author_list = tk.Listbox(root, font=("Times Roman", 12), width=20)
    author_list.place(x=320, y=200) 

    copies_list = tk.Listbox(root, font=("Times Roman", 12), width=10)
    copies_list.place(x=520, y=200)

    scrollbar = tk.Scrollbar(root, command=lambda *args: (book_list.yview(*args), author_list.yview(*args), copies_list.yview(*args)))
    scrollbar.place(x=575, y=201, height=201)

    book_list.config(yscrollcommand=scrollbar.set)
    author_list.config(yscrollcommand=scrollbar.set)
    copies_list.config(yscrollcommand=scrollbar.set)

    back_btn = tk.Button(root, text="Back", font=("Times Roman", 14), command=lambda: main_interface(root))
    back_btn.place(x=250, y=440)

    for book in open("books.txt", "r").readlines():
        book_name, author_name, copies = book.strip().split("||")
        book_list.insert(tk.END, book_name)
        author_list.insert(tk.END, author_name)
        copies_list.insert(tk.END, copies)

    book_entry.bind("<KeyRelease>", lambda event: update_inventory_list(book_entry, author_entry, book_list, author_list, copies_list))
    author_entry.bind("<KeyRelease>", lambda event: update_inventory_list(book_entry, author_entry, book_list, author_list, copies_list))

def update_inventory_list(book_entry, author_entry, book_list, author_list, copies_list):
    book_list.delete(0, tk.END)
    author_list.delete(0, tk.END)
    copies_list.delete(0, tk.END)
    with open("books.txt", "r") as book_db_file:
        book_list_data = book_db_file.readlines()
        for book in book_list_data:
            book_name, author_name, copies = book.strip().split("||")
            if book_entry.get().strip().lower() in book_name.lower() and author_entry.get().strip().lower() in author_name.lower():
                book_list.insert(tk.END, book_name)
                author_list.insert(tk.END, author_name)
                copies_list.insert(tk.END, copies)


# main interface
def main_interface(root):

    for widget in root.winfo_children():
        widget.destroy()


    # Default screen label
    label = tk.Label(root, text="Welcome to the Library Management System", font=("Times Roman", 16))
    label.pack(pady=40)

    # Buttons for different functionalities
    BOOK_MGMT = tk.Button(root, text="Book Management", font=("Times Roman", 14), command=lambda: BOOK_MGMT_INTERFACE(root))
    BOOK_MGMT.pack(pady=10)
    USER_MGMT = tk.Button(root, text="User Management", font=("Times Roman", 14), command=lambda: USER_MGMT_INTERFACE(root))
    USER_MGMT.pack(pady=10)
    ISSUE_RETURN = tk.Button(root, text="Issue/Return Books", font=("Times Roman", 14), command=lambda: ISSUE_RETURN_INTERFACE(root))
    ISSUE_RETURN.pack(pady=10)
    INVENTORY = tk.Button(root, text="View Inventory", font=("Times Roman", 14), command=lambda: INVENTORY_INTERFACE(root))
    INVENTORY.pack(pady=10)


def main(): 
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("600x500")
    main_interface(root)
    root.mainloop()


main()