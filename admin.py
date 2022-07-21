from register import *
import re
class DataBase:
    def __init__(self):
        self.data = []
        self.read_data()
    
    def read_data(self):
        with open('db.txt', 'r') as file:
            for line in file:
                line = line.strip().split(',')
                self.data.append(line)
    
    def show_data(self):
        for line in self.data:
            print(line)
    
    def delete_data(self, num):
        with open('db.txt', 'w') as file:
            for line in self.data:
                if line[0] != num:
                    file.write(','.join(line) + '\n')

    def update_data(self, num, name, email, program):
        with open('db.txt', 'w') as file:
            for line in self.data:
                if line[0] == num:
                    line[1] = name
                    line[2] = email
                    line[3] = program
                    file.write(','.join(line) + '\n')
                else:
                    file.write(','.join(line) + '\n')


    
def admin_pannel():
    while True:
        print('--- please choose your option by entering the number ---')
        print('1.Show all data')
        print('2.Add new data')
        print('3.Delete data')
        print('4.Update data')
        print('5.Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            db = DataBase()
            db.show_data()
        elif choice == '2':
            print('Enter your details to add new data')
            name = input('Enter your name: ')
            while not re.match(r'^[a-zA-Z ]+$', name):
                print('Name must only contain letters')
                name = input('Enter your name: ')
            email = input('Enter your email: ') 
            while not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
                print('Please enter a valid email')
                email = input('Enter your email: ')
            program= input('Enter your prefered program:')
            while not re.match(r'^[a-zA-Z ]+$', program):
                print('Program must only contain letters')
                program = input('Enter your prefered program:')
            new_user=User(name, email, program)
            new_user.register()


        elif choice == '3':
            '''delete data from db.txt by thier number as input from user'''
            db = DataBase()
            db.show_data()  
            num= input('Enter the num of the user you want to delete: ')
            db.delete_data(num)

        elif choice == '4':
            '''update data from db.txt by thier number as input from user'''
            db = DataBase()
            db.show_data()  
            num= input('Enter the num of the user you want to update: ')
            name = input('Enter new name to be updated: ')
            while not re.match(r'^[a-zA-Z ]+$', name):
                print('Name must only contain letters')
                name = input('Enter new name to be updated: ')
            email = input('Enter new email to be updated: ') 
            while not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', email):
                print('Please enter a valid email')
                email = input('Enter new email to be updated: ')
            program= input('Enter new program to be updated:')
            while not re.match(r'^[a-zA-Z ]+$', program):
                print('Program must only contain letters')
                program = input('Enter new program to be updated:')
            db.update_data(num, name, email, program)
        elif choice == '5':
            exit()  
        else:
            print('Invalid choice')
            