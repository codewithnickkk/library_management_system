name = []
author = []
price = []

def options():
    print()
    print('Select Options to Perform')
    print('1.Add Book')
    print('2.Get Book')
    print('3.Update Book')
    print('4.Remove Book')
    print('0.Exit')
    return opt()

def add():
    print()
    Book_name = input('Enter Book Name: ')
    Book_author = input('Enter Author Name: ')
    Book_price = float(input('Enter Book Price: '))
    global name, price, author
    name.append(Book_name)
    price.append(Book_price)
    author.append(Book_author)
    print('Book Added')
    return options()

def get():
    print()
    Book_name = input("Enter Book Name You're Looking For: ")
    global name, author, price
    
    if Book_name in name:
        print('Book is Available')
        index = name.index(Book_name)
        print('Book: ',name[index])
        print('Author: ',author[index])
        print('Price: ',price[0])
    else:
        print('Book is Not Available')
    return options()

def update():
    print()
    Book_name = input("Enter Book Name You Want to Update: ")
    global name, price, author
    
    if Book_name in name:
        print('Book is Available')
        print('What to Update ?')
        print('1.Book Name')
        print('2.Author Name')
        print('3.Book Price')
        
        opt = int(input('Enter Digit Respective to Desired Option: '))
        
        if opt == 1:
            updated_name = input('Enter Updated Book Name: ')
            index = name.index(Book_name)
            name[index] =  updated_name
            print('Book Name Updated Successfully')
        elif opt == 2:
            updated_Author = input('Enter Updated Author Name: ')
            index = name.index(Book_name)
            author[index] =  updated_Author
            print('Book Author Updated Successfully')

        elif opt == 3:
            updated_price = input('Enter Updated Book Price: ')
            index = name.index(Book_name)
            price[index] =  updated_price
            print('Book Price Updated Successfully')

        else:
            print('error occured')
              
    else:
        print('Book is Not Available')
    return options()

def remove():
    print()
    Book_name = input('Enter Book Name to Remove: ')
    global name 
    if Book_name in name:
        print('Book is Available') 
        name.remove(Book_name)
        print('Book Removed')       
    else:
        print('Book is Not Available')
  
    return options()

def opt():
    print()
    opt = get_number('Enter Digit Respective to Desired Option: ')

    if opt == 1:
        return add()
    elif opt == 2:
        return get()
    elif opt == 3:
        return update()
    elif opt == 4:
        return remove()
    elif opt == 0:
        return 0
    else:
        print('Invalid Option')
        
def get_number(prompt="Enter a number: "):
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid syntax. Please enter a valid number.")
     
            
input('Enter Name of Library: ')
input('Enter Address of Library: ')
pincode = get_number('Enter Pincode: ')

options()

