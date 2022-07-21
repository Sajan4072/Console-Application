'''This is tha main landing console  '''
from register import *
from login import *
from admin import *
def main():
    print('\t \t \t \t \t \t\t \t***** Welcome to Insight Workshop Academy *****')
    print('\n ')
    print('Please choose your option by entering the number')
    print('1 - Register for a program')
    print ('2 - Login as an admin')
    print ('3 - Exit')
    pass
    
    choice = input('Enter your choice: ')
    if choice == '1':
        register_user()
    elif choice == '2':
        print('For logging in as an admin, please enter your details')
        name = input('Enter admin name: ')
        password = input('Enter admin password: ')
        admin = Admin(name, password)
        print(admin.login())
        if admin.login() == True:
            admin_pannel()
    elif choice == '3':
        exit()
    else:
        print('Invalid choice')
        


if __name__=="__main__":
    main()   