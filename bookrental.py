class BookRentalSystem():
    def __init__(self,list_of_books,Bookstore_name):
        # creating a dictionary of all books keys
        self.sum=0
        self.rent_data = {}
        self.list_of_books = list_of_books
        self.Bookstore_name = Bookstore_name
        self.return_list={}
        self.offer=None

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No reader have lend this book
            self.rent_data[books] = 'Not assigned'

    def display_books(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index+1}:{books}")

    def rent_book(self,book,reader,offer):
        self.offer=offer
        if (self.rent_data[book] == 'Not assigned'):
            x = input("How do you want to rent the book: \n 1.Hourly basis(12 rupees per hour) \n 2.Daily basis(15 rupees per day) \n 3.Weekly basis(30 rupees per week)\n")
            if x == "1":
                period='hour'
                time=input("Enter the number of hours you want to rent for:\n")
                self.bill(book,time,period)
            elif x == "2":
                period='day'
                time=input("Enter the number of days you want to rent for:\n")
                self.bill(book,time,period)
            elif x == "3":
                period='week'
                time=input("Enter the number of weeks you want to rent for:\n")
                self.bill(book,time,period)
            else:
                print('Enter the right option:\n')
            self.rent_data.update({book:reader})
            print("\n Rent Approved \n")

        elif (self.rent_data[book]!='Not assigned'):
            print(f"Sorry this book is being currently rented by {self.rent_data[book]}\nCheck out the other books{self.list_of_books.remove(book)}")
            # quit()
        else:
            print("You have written wrong book name")
    
    def return_book(self,book):
        if book in self.list_of_books:
            if (self.rent_data[book] != 'Not assigned'):
                self.rent_data[book]='Not assigned'
                print("Your payment is ",self.return_list[book])
                self.return_list.pop(book)
            else:
                print("Sorry but it is currently not available")
        else:
            print("You have written wrong book name")
        

    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        self.rent_data[book_name] = None

    def delete_book(self,book_name):
        self.list_of_books.remove(book_name)
        self.rent_data.pop(book_name)

    def bill(self,book,time,period):
        if (period=='hour'):
            amt=int(time)*12
            if(self.offer==0):
                print(f'Your total is {amt} rupees \n Make sure to return the book on time') 
                self.return_list[book]=amt
            else:
                print(f'Your total is {amt-0.3*amt} rupees \n Make sure to return the book on time') 
                self.return_list[book]=amt-0.3*amt
            self.sum=self.sum+ amt 

        elif (period=='day'):
            amt=int(time)*15
            if(self.offer==0):
                print(f'Your total is {amt} rupees \n Make sure to return the book on time') 
                self.return_list[book]=amt
            else:
                print(f'Your total is {amt-0.3*amt} rupees \n Make sure to return the book on time') 
                self.return_list[book]=amt-0.3*amt
            self.sum=self.sum+ amt 
        else:
            amt=int(time)*30
            if(self.offer==0):
                print(f'Your total is {amt} rupees \n Make sure to return the book on time') 
                self.return_list[book]=amt
            else:
                print(f'Your total is {amt-0.3*amt} rupees \n Make sure to return the book on time') 
                self.return_list[book]=amt-0.3*amt
            self.sum=self.sum+ amt 

def main():
    list_books = ['a','b','c','d','e','f','g','h','i','j','k']
    Bookstore_name = 'Book Rental Store'
    password = 123456

    BRS = BookRentalSystem(list_books,Bookstore_name)

    print(f"Welcome To {BRS.Bookstore_name} library\n ")
    name = input("Enter your name:\n")

    Exit = False
    while (Exit is not True):
        _input = input("Enter your choice:\n 1.Display Book \n 2.Rent book \n 3.Return book \n 4.Add Book \n 5.Delete Book  \n Press q for exit")
        print("\n")

        if _input == "q":
            Exit = True

        elif _input == "1":
            BRS.display_books()

        elif _input == "2":
            print("We are offering our customers 30 percent off on rent of 3/4/5 books ")
            print('The available books are',BRS.list_of_books-BRS.return_list.keys())
            no_of_books= int(input("How many books do you want to rent:\n"))
            if(no_of_books==1 or no_of_books==2):
                offer=0
                book = input("Enter the book you want to rent:\n")
                BRS.rent_book(book,name,offer)
                no_of_books-=1
                if(no_of_books!=0):
                    book = input("Enter the book you want to rent:\n")
                    BRS.rent_book(book,name,offer)
                print("total:",BRS.sum)
            elif(no_of_books==3 or no_of_books==4 or no_of_books==5):
                offer=1
                book = input("Enter the book you want to rent:\n")
                BRS.rent_book(book,name,offer)
                x=no_of_books
                while(x>0):
                    book = input("Enter the book you want to rent:\n")
                    BRS.rent_book(book,name,offer)
                    x=x-1
                print("Total amount to be payed on return is:",BRS.sum-(0.3*BRS.sum))
            else:
                print("You can rent maximum of 5 books in a day")
            # BRS.rent_book(_input3,_input2)

        elif _input == "3":
            _input2 = input("Which Book do you want to return:\n")
            BRS.return_book(_input2)

        elif _input == "4":
            _input2 = input("Book name:")
            BRS.add_book(_input2)

        elif _input == "5":
            _input_password = int(input("Write the password to delete:\n"))
            if (_input_password == password):
                _input2 = input("Which book do you want to delete:\n")
                BRS.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        else:
            print('Enter the right choice')
            continue
if __name__ == "__main__":
    main()
""""A Book Rental System : A full fledged Book rental system implemented in Python using object oriented programming.
a.	Customers can
i.	See available Books on the shop
ii.	Rent Books on hourly basis 12 rupees per hour.
iii.	Rent Books on daily basis 15 rupees per day.
iv.	Rent Books on weekly basis Rupees 30 per week.
b.	Family Rental : 
i.	a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price
c.	The Book rental shop can
i.	issue a bill when customer decides to return the Book.
ii.	display available inventory
iii.	take requests on hourly, daily and weekly basis by cross verifying stock.
"""