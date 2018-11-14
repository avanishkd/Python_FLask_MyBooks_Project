class signup_dto():
    '''
    DTO Layer of Signup
    '''
    __user_name = ""
    __age = ""
    __email_id = ""
    __password = ""
    __confirm_password = ""
    __phone_num = ""
    __address = ""
    __role = ""
    __feedback = []
    __booklist = []
    __rating = ""
    __addhar = ""


    def __init__(self):
        '''
        constructor called automatically
        '''
        pass


    def set_values_buyer(self,user_name,age,email_id,password,confirm_password,phone_num,address,role):
        '''
        passing the required fields for signing up of buyer
        :param user_name: String
        :param age: Integer (age of the buyer)
        :param email_id: String (email ID  of the buyer)
        :param password: String (Password of the buyer)
        :param confirm_password: String (confirming the given password)
        :param phone_num: Integer (contact details of the buyer)
        :param address: String (Address of the buyer)
        :param role: String (determining whether a buyer or seller)
        '''
        signup_dto.__user_name = user_name
        signup_dto.__age = age
        signup_dto.__email_id = email_id
        signup_dto.__password = password
        signup_dto.__confirm_password = confirm_password
        signup_dto.__phone_num = phone_num
        signup_dto.__address = address
        signup_dto.__role = role


    def get_values_buyer(self):
        '''
        Extracting the values passed from dao layer of buyer
        :return: user_name, age, emailID, password, confirm password, phone_number, address, role
        '''
        return (signup_dto.__user_name, signup_dto.__age, signup_dto.__email_id, signup_dto.__password, signup_dto.__phone_num, signup_dto.__address, signup_dto.__role)


    def set_values_seller(self,user_name,age,email_id,password,confirm_password,phone_num,address,role,addhar):
        '''
        passing the required fields for signing up of seller
        :param user_name: String
        :param age: Integer (age of the seller)
        :param email_id: String (email ID  of the seller)
        :param password: String (Password of the seller)
        :param confirm_password: String (confirming the given password)
        :param phone_num: Integer (contact details of the seller)
        :param address: String (Address of the seller)
        :param role: String (determining whether a buyer or seller)
        '''
        signup_dto.__user_name = user_name
        signup_dto.__age = age
        signup_dto.__email_id = email_id
        signup_dto.__password = password
        signup_dto.__confirm_password = confirm_password
        signup_dto.__phone_num = phone_num
        signup_dto.__address = address
        signup_dto.__role = role
        signup_dto.__addhar = addhar

    def get_values_seller(self):
        '''
        Extracting the values passed from dao layer of seller
        :return: user_name, age, emailID, password, confirm password, phone_number, address, role
        '''
        return (signup_dto.__user_name, signup_dto.__age, signup_dto.__email_id, signup_dto.__password, signup_dto.__phone_num, signup_dto.__address,  signup_dto.__role,signup_dto.__addhar)

    def set_values_email(self,email_id):
        """
        :param email_id:
        """
        signup_dto.__email_id = email_id


    def get_values_email(self):
        '''
        Extracting the values passed from dao layer of seller
        :return:
        '''
        return signup_dto.__email_id