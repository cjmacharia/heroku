import unittest
from user import User

class Usertest(unittest.TestCase):
    """
        Class performing unit testing for class User
    """

    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.newUser = User()

    def test_create_account(self):
        """defining method to test for creating user account"""
        self.newUser.users = {}
        result = self.newUser.register( 'email@mail.com', 'name', 'cj', 'cj')
        self.assertEqual(1, result, "User succesfully created")   

    def test_register_null_name(self):
        """defining method to test for creating user account with an empty name field"""
        output=self.newUser.register('test@email.com','','pass','pass')
        self.assertEqual(5, output, "Please fill your name")

    def test_register_null_email(self):
        """defining method to test for creating user account with an empty email"""
        output=self.newUser.register('','name','pass','pass')
        self.assertEqual(5, output, "Email is Empty ")    
        
    def test_null_password(self):
        """ defining method to test for creating user account with an empty passsword field"""
        output=self.newUser.register('test@email.com','mash','','pass')
        self.assertEqual(5, output, "Please the password filed") 
 
    def test_cpassword_is_password(self):
        """defining method to test for created user's password is equal to confirm password"""
        output=self.newUser.register('test@email.com', 'cj', 'pass', 'pss')    
        self.assertEqual(3, output, "password mismatch")    

    def test_wrong_login_password(self):
        """defining method to test if login password is equal to register passsword"""
        self.newUser.users = {}
        self.newUser.register( 'email@mail.com', 'cj','pass', 'pass')
        result = self.newUser.login('email@mail.com', 'pass123')
        self.assertEqual(2, result,"password mismatch") 

    def test_wrong_login_email(self):
        """defining method to test if login email is equal to register email"""
        self.newUser.users = {}
        self.newUser.register('cj', 'email@mail.com', 'pass', 'pass')
        result = self.newUser.login('cj@gmail.com', 'pass')
        self.assertEqual(3, result, "wrong email try again") 

    def test_login_null_email(self):
        """defining method to test for null login email"""
        result = self.newUser.login('', 'pass')
        self.assertEqual(4, result, "Please fill the email field")   

    def test_login_null_password(self):
        """defining method to test for null login password"""
        result = self.newUser.login('cj@gmail.com', '')
        self.assertEqual(4, result, "Please fill the password field")    
 
    def test_existing_useremail(self):
        """defining method to test for an existing user """
        self.newUser.users = {}
        self.newUser.register('email@mail.com','cj', 'pass', 'pass')
        result = self.newUser.register('email@mail.com', 'mash', 'pass123', 'pass123')
        self.assertEqual(4, result, "user already exists")


if __name__ == "__main__":
    unittest.main()        