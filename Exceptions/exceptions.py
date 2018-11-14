'''
Custom Exceptions
'''
class Aadhar_Invalid(Exception):
    '''
        Exception occurs when password and confirm password are not matching
    '''
    def return_message(self):
        return "Aadhar number should be of 11 digits"
        
class Age_Invalid(Exception):
    '''
        Exception occurs when entered age is invalid
    '''
    def return_message(self):
        return "Invalid Age: Enter only digits"

class Password_mismatch(Exception):
    '''
        Exception occurs when password and confirm password are not matching
    '''
    def return_message(self):
        return "Entered Passwords did not match "


class Pymongo_Error(Exception):
    '''
        Exception occurs when there is some error updating in the database
    '''

    def return_message(self):
        return "Syntax Error for database queries"


class User_Already_Present(Exception):
    '''
        Exception occurs when user is already present in database at the time of signing up
    '''
    def return_message(self):
        return "Already present"


class Email_Id_Invalid(Exception):
    '''
        Exception occurs when Email Id format is not correct
    '''
    def return_message(self):
        return "Invalid Email Id format"


class Phone_Number_Invalid(Exception):
    '''
        Exception occurs when Phone Number is not of Valid format
    '''
    def return_message(self):
        return "Invalid Phone Number"


class Mandatory_Fields(Exception):
    '''
        Exception occurs when All the Mandatory fields are not present
    '''
    def return_message(self):
        return "All mandotary fields are required"


class Invalid_Password(Exception):
    """
        Exception class for throwing catching exception when invalid password is entered
    """
    def return_message(self):
        return "Please Enter Correct Format For Password(8-16 character,atleast 1 uppercase and spcl char)"


class Invalid_number(Exception):
    """
        Exception class for throwing catching exception when invalid phone is entered
    """
    def return_message(self):
        return "Number Should be of 10 digits"


class Wrong_phone_number(Exception):
    """
        Exception class for throwing catching exception when wrong phone number is entered
    """
    def return_message(self):
        return "Phone number did not match the already signed up number"


class Email_id_not_present(Exception):
    """
        Exception class for throwing catching exception when email is not present in the database
    """
    def return_message(self):
        return "Please Sign UP"


class Book_Already_Present(Exception):
    """
        Exception class for throwing catching exception when book is already present in the database
    """
    def return_message(self):
        return "Already present"


class ISBN_not_correct(Exception):
    """
        Exception class for throwing catching exception when email is not present in the database
    """
    def return_message(self):
        return "Kindly Provide correct ISBN for books"

			
class Email_Check(Exception):
    """
        Exception class for throwing catching exception when email is not present in the database
    """
    def return_message(self):
        return "Seller Email Id is not present in the database. Please Check your Email ID"


class Seller_Email_check(Exception):
    """
        Exception class for throwing catching exception when email is not present in the seller database
    """
    def return_message(self):
        return "Seller Email Id is not present in the database. Please sign up"


class Bookname_check(Exception):
    """
        Exception class for throwing catching exception when book is not available in the database
    """
    def return_message(self):
        return "Book is not available in the database"


class Book_Count(Exception):
    """
        Exception class for throwing catching exception when no book is available in the seller stock
    """
    def return_message(self):
        return "No book available in the stock"

