
list_of_names=[]
list_of_DOB=[]
list_of_contact_num=[]
list_of_email=[]
list_of_password=[]
borrowers_list=[list_of_names,list_of_DOB,list_of_contact_num,list_of_email,list_of_password]
book_info={"101":{"Name":"Network Theory","Author": "Sadiku","Total_copies":50,"Copies_available":50,"ISBN":1234567891234,"Published year":2001},
            "102":{"Name":"EDC","Author":"Neamen","Total_copies":320,"Copies_available":320,"ISBN":9087654321123,"Published year":2005},
             "103":{"Name":"Engineering Maths","Author":"Dr.B.S.Grewal","Total_copies":90,"Copies_available":0,"Published year":2008}}
pos=0
borrower_history={}
currently_taken_book={}
b={}
from datetime import date,timedelta

class borrower:
    def __init__(self):
        pass
    def  register(self):
        self.name()
        self.DOB()
        self.contact_num()
        self.email()
        self.password()
        print("Your account has been created!")
        
    def name(self):
        print("enter your name")
        x=input()
        list_of_names.append(x)
    def DOB(self):
        print("enter your date of birth in format dd-mm-yyyy")
        DOB=input().split("-")
        list_of_DOB.append(DOB)
    def contact_num(self):
            print("enter contact number")
            num=input()
            import re
            if (re.search("[0-9]{10}",num)):
                list_of_contact_num.append(num)
                return
            else:
                print("contact number is 10 digits number ,fill it again")
                self.contact_num()
    def email(self):
            print("enter email address")
            email_add=input()
            import re
            if( re.search("^[a-zA-Z]+[0-9]+.*@gmail.com$",email_add)):
                list_of_email.append(email_add)
                return
            else:
                print("email_address must start with an alphabet ,then it shoulh have one or more digit and  should have a domain @gmail.com")
                self.email()
    def password(self):
            print("enter your password")
            word=input()
            import re
            if(re.search("[a-zA-Z]+[0-9]+.",word)):
                list_of_password.append(word)
                return
            else:
                print("password must begin with an alphabet ,must contain one or more digit and a special character")
                self.password()
    def login_user(self):
        print("enter your email address")
        x=input()
        if x in list_of_email:
            print("enter password")
            y=input()
            if y==list_of_password[list_of_email.index(x)]:
                print("enter 1 to view the books you have taken \nenter 2 to see details of books available in the library \nenter 3 to see all the books you have taken in the past")
                z=int(input())
                if z==1:
                    if currently_taken_book[x]==None:
                        print("You have not taken any book ")
                    else:
                        print(currently_taken_book[x])
                elif z==2:
                    print(book_info)
                elif z==3:
                    print(borrower_history)
            else:
                print("password does not match with the email id")
        else:
            print("the email id is not registered")
    
class admin:
    def __init__(self):
        pass
    def login_admin(self):
        print("enter your email id")
        x=input()
        if x=="admin":
            y=input("enter your password")
            if y=="admin":
                self.admin_functions()
            else:
                print("Invalid password")
        else:
            print("Email id is not registered")
            self.login_admin()
    def admin_functions(self):
            print("enter 1 to create borrowers\n enter 2 to view book details \n enter 3 to add more books to library \n enter 4 to view borrowers information \n enter 5 to lend a book to borrower \n enter 6 to edit book information \n enter 7 to accept book return")
            x=int(input())
            if x==1:
                y=borrower()
                y.register()
                if input("Do you want to be here more ,enter yes")=="yes":
                    self.admin_functions()
                else:
                    return
            elif x==2:
                print(book_info)
                if input("Do you want to be here more ,enter yes")=="yes":
                    self.admin_functions()
                else:
                    return
            elif x==3:
                self.add_more_books()
                if input("Do you want to be here more ,enter yes")=="yes":
                    self.admin_functions()
                else:
                    return
            elif x==4:
                self.show_borrowers_info()
                if input("Do you want to be here more ,enter yes")=="yes":
                    self.admin_functions()
                else:
                    return
            elif x==5:
                self.borrowing_book()
                if input("Do you want to be here more ,enter yes")=="yes":
                    self.admin_functions()
                else:
                    return
            elif x==6:
                self.edit_book_info()
                if input("Do you want to be here more ,enter yes")=="yes":
                    self.admin_functions()
                else:
                    return
            elif x==7:
                self.book_return()
                if input("Do you want to be here more ,enter yes")=="yes":
                    self.admin_functions()
                else:
                    return

   
    def add_more_books(self):
        a={}
        book_info[input("enter book id")]=a
        a["Name"]=input("enter name of book")
        a["Author"]=input("enter Author of book")
        a["Total_copies"]=int(input("enter total number of copies"))
        a["Copies_available"]=a["Total_copies"]
        a["ISBN"]=int(input("enter ISBN of book"))
        a["Published year"]=int(input("enter published year of book"))

    def edit_book_info(self):
        print("enter id of book you want to make changes on ")
        x=input()
        if x not in book_info:
            print("There is no book with this id")
        else:
            print(book_info[x])
            print("enter 1 to change the name \n enter 2 to change the Author \n enter 3 to change the number of copies \n enter 4 to edit number of currently available copies \n enter 5 to change the ISBN \n enter 6 to Change the Published year of book \n enter 7 to delete the book from the library")
            y=int(input())
            if y==1:
                book_info[x]["Name"]=input("enter new name")
            elif y==2:
                book_info[x]["Author"]=input("enter new Author")
            elif y==3:
                book_info[x]["Total_copies"]=int(input("enter total number of copies if this book in the library"))
            elif y==4:
                 book_info[x]["Copies_available"]=int(input("enter currently avaialable copies of this book "))
            elif y==5:
                 book_info[x]["ISBN"]=int(input("enter new ISBN"))
            elif y==6:
                 book_info["Published year"]=int(input("enter published year"))
            elif y==7:
                 del book_info[x]
            else:
                print("Data has been updated")
                return
    def show_borrowers_info(self):
        print("enter the name")
        x=input()
        if x in list_of_names:
            pos=list_of_names.index(x)
            print("NAME",list_of_names[pos])
            print("DOB",list_of_DOB[pos])
            print("contact number",list_of_contact_num[pos])
            print("EMAIL ID ",list_of_email[pos])
            if list_of_email[pos] in borrower_history:
                print(borrower_history[list_of_email[pos]])
        else:
            print("Borrower does not exist")
            
    def borrowing_book(self):
        x=input("enter borrowers email id")
        if x in list_of_email:
            z=list_of_email.index(x)
            print("enter the book id")
            y=input()
            if y in book_info:
                if book_info[y]["Copies_available"] != 0:
                    #b={}
                    borrower_history[x]=b
                    b["Name"]=book_info[y]["Name"]
                    d=date.today()
                    b["Issue_date"]=str(d)
                    b["due date"]=str(d+timedelta(days=14))
                    currently_taken_book=b
                    b["Name"]=book_info[y]["Name"]
                    d=date.today()
                    b["Issue_date"]=str(d)
                    b["due date"]=str(d+timedelta(days=14))
                    book_info[y]["Copies_available"]=book_info[y]["Copies_available"]-1
                else:
                    print("book is not available")
            else:
                print("No such book with this id exists in the library")
        else:
            print("This email id is not registered")
            print("Do you want to try again")
            if input()=="yes":
                self.borrowing_book()
            else:
                return
    def book_return(self):
        x=input("enter borrowers email id")
        if x in borrower_history:
            print("enter the book id")
            y=input()
            if borrower_history[x]["Name"]==book_info[y]["Name"]:
                currently_taken_book[x]=0
                book_info[y]["Copies_available"]+=1
                d=date.today()
                if d>b[due_date]:
                    print("You have to pay fine of  INR 200")
            else:
                print("You have not taken this book")
        else:
            print("such email id student is not registered")

            
def permission():           
        print("Enter 1 to enter as admin or a enter 2 to enter as  user")
        x=int(input())
        if x==1:
            u=admin()
            u.login_admin()
            permission()
        elif x==2:
            student=borrower()
            print("Do you want to register or login ,enter 1 to register or enter 2 to login")
            a=int(input())
            if a==1:
                student.register()
                permission()
            elif a==2:
                student.login_user()
                permission()
        else:
            return
permission()
                
    
    


            
            
            

            