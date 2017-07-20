import re

users = {'foo@gmail.com': {'name': 'dsd', 'email': 'foo@gmail.com', 'pass': 'a'}}

class User(object):
    """
    Class to regihandle  user functions
    """

    def __init__(self, name=None, email=None, password=None):
        """ Initializing  class instance variables"""
        self.name = name
        self.email = email
        self.password = password

    def register(self, email, name, password, cpassword):
        """defining method to create account"""           
        if  name != '' and email != '' and password != '':
            if email not in users.keys():
                if password == cpassword:
                    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                    result = email
                    if re.search(regex, result):
                        users[email] = {
                        'name': name,
                        'email': email,
                        'pass': password,
                        }
                        print(users)
                        return  1                       
                    else:
                        return 2 
                else:
                    return 3
            else:
                return 4
        else:
            return 5
             
    def login(self, email, password):
        """ defining method to validate user"""
        if email != '' and password != '':
            if email in users.keys():
                result = users[email]
                pword = result['pass']
                if pword == password:
                    return 1
                else:
                    return 2
            else:
                return 3
        else:
            return 4  
            
    def get_user_name(self, email):
        """function to get a user's name"""
        if email in users.keys():
            result = users[email]
            return result['name']
        else:
            return False

    def get_user_email(self, email):
        """function to get a user's email"""
        if email in users.keys():
            result = users[email]
            return result['email']
        else:
            return False