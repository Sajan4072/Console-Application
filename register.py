'''this handles register function'''
from http import server
import re
import smtplib
from decouple import config
'''class for user registration for particular program'''
class User:
    def __init__(self, name, email, program):
        '''assign numbers to each user automatically'''
        self.number = len(open('db.txt', 'r').readlines()) + 1
        self.name = name
        self.email = email
        self.program =program

    def register(self):
        with open('db.txt', 'a') as file:
            file.write(f'{self.number},{self.name},{self.email},{self.program}\n')
        '''send email to user'''
        # sender_email=config('SENDER_MAIL')
        # print(sender_email)
        # receiver_email=self.email
        # password=config('SENDER_PASSWORD') 
        # print(password)
        message=f'Hi {self.name},\n\nThank you for registering for {self.program} program.\n\nRegards,\nInsight Workshop Academy'
        
        # server=smtplib.SMTP('smtp.gmail.com',587)
        # server.starttls()
        # server.login(sender_email,password)
        # server.sendmail(sender_email,receiver_email,message)

        return f'{self.name} has been registered'
        



'''console that displays the menu 1.register for a program 2.exit'''
def register_user():
    while True:
        print('\t \t \t \t \t \t\t \t***** Welcome to Insight Workshop Academy Registrtion page *****')
        print('\n ')
        print('1.Register for a program')
        print('2.Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            print('For registering for a program, please enter your details')
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

            user = User(name, email, program)
            print(user.register())
        elif choice == '2':
            break
        else:
            print('Invalid choice')

# if __name__=="__main__":
#     main()   