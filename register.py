
'''class for user registration for particular program'''
class User:
    def __init__(self, name, email, program):
        self.name = name
        self.email = email
        self.program =program

    def register(self):
        with open('db.txt', 'a') as file:
            file.write(f'{self.name},{self.email},{self.program}\n')
        return f'{self.name} has been registered'



'''console that displays the menu 1.register for a program 2.exit'''
def main():
    while True:
        print('1.Register for a program')
        print('2.Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            name = input('Enter your name: ')
            email = input('Enter your email: ')
            program= input('Enter your prefered program:')
            user = User(name, email, program)
            print(user.register())
        elif choice == '2':
            break
        else:
            print('Invalid choice')

if __name__=="__main__":
    main()   