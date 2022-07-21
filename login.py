'''class to login as an admin by checking if name and password mathches or not from admin.txt'''
class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def login(self):
        with open('admin.txt', 'r') as file:
            '''error handling for list index out of range'''
            try:
                for line in file:
                    line = line.strip().split(',')
                    if self.name.lower() == line[0].lower() and self.password == line[1]:
                        return True
                        
            except IndexError:
                print('Invalid name or password')
                return 'Invalid name or password'
        return 'Invalid name or password'