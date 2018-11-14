from DAO import DaoUser#importing dao user layer
from Service import ServiceInterface#importing service interface layer
from interface import implements#importing interface
from Exceptions import exceptions#importing exceptions layer
from DTO import login_dto,signup_dto,change_password_dto#importing dto layer
from LogConfig import log_file as log#importing log configuration layer
import re#importing regular expression

class ServiceImpl(implements(ServiceInterface.ServiceInterface)):
    def __init__(self):
        '''
        contructor called automatically
        '''
        pass
    
    def age_validation(self,age):
        val = age.isdigit()
        return val

    def password_validation(self,password,confirm_password):
        '''
        :param password: user password
        :param confirm_password: user renter password
        checking whether the password and confirm password is equal or not
        :return: boolean either true or false
        '''
        if(password==confirm_password):
            return True
        else:
            return False

    def email_validation(self,email_id):
        '''
        :param email_id: user email id
        checking whether the email id is correct format or not , eg. abc@gmail.com
        :return: boolean either true or false
        '''
        match = re.compile(r"[\w\.-]+@[\w\.-]+")
        if match.search(email_id):
            return True
        else:
            return False

    def contact_details_validation(self,phone_num):
        '''
        :param phone_num: user contact details
        checks whether the contact detail entered by user is of 10 digit or not(i.e. in correct form)
        :return: boolean value either true or false
        '''
        match = re.search(r"^\d{10}",phone_num)
        if match == None:
            return False
        else:
            return True

    def aadhar_validation(self,aadhar):
        """
        Method to check that the entered aadhar number is of 11 digits
        :param aadhar number:
        :return: True if number is validated else false
        """
        match = re.search(r"^\d{11}", aadhar)
        if match == None:
            return False
        else:
            return True


    def checking_password(self,password):
        '''
        :param password: user password
        checks whether the password is in correct format: length>8 & length<16 letters, atleast one capital alphabet, digit and special character
        :return: boolean value either true or false
        '''
        temp_password = password
        length_password = len(password)
        count = 0
        if length_password >= 8 and length_password <= 16:
            count += 1
        if re.findall('[A-Z]', temp_password):
            count += 1
        if re.findall('[@_!#$%^&*()<>?/\|}{~:]', temp_password):
            count += 1
        if re.findall('[a-z]', temp_password):
            count += 1
        if re.findall('[0-9]', temp_password):
            count += 1

        if count == 5:
            return True
        else:
            return False

    def mandatory_fields(self, user_name, age, email_id, password, confirm_password,phone_num, address, role):
        '''
        checks all the mandatory fields are passed in json object
        :param user_name: user name which will be shown on website (String)
        :param age: age of the user (Integer)
        :param email_id: email id of the the user(String)
        :param password: password of the user(String)
        :param confirm_password: re-entering the password for verification(String)
        :param phone_num: contact details of user(Integer)
        :param address: address of the user(String)
        :param preferences: what the user prefer(String)
        :param role: role as buyer or seller(String)
        :return:boolean either true or false
        '''
        if user_name == "" or age == "" or email_id == "" or password == "" or confirm_password == "" or phone_num == "" or address == ""  or role == "":
            return False
        else:
            return True


    def check_user(self,data):
        '''
        check whether the user id already present in the database
        :param data: json object containing user details
        :return: boolean either True or False
        '''
        try:
            x= data["Username"]
            try:
                raise exceptions.User_Already_Present()
            except exceptions.User_Already_Present as e:
                log.logger.warning(e.return_message())
                return e.return_message()
        except TypeError as e:
            return "False"


    def signup_detail(self,request_data):
        '''
        signup details of the buyer and seller
        :param request_data: json object
        :return:response from the database after validating all the fields
        '''
        log.logger.info("In sign up function in service layer")
        ob_dao = DaoUser.DaoImpl()
        ob_dto = signup_dto.signup_dto()
        role = request_data['Role']
        user_name = request_data['Username']
        age = request_data['Age']
        email_id = request_data['Email_Id']
        password = request_data['Password']
        confirm_password = request_data['Confirm_Password']
        phone_num = request_data['Phone Number']
        address = request_data['Address']
        if role == "Buyer" or role == "Seller":
            if (self.mandatory_fields(user_name, age, email_id, password, confirm_password, phone_num, address, role) == False):
                try:
                    raise exceptions.Mandatory_Fields()
                except exceptions.Mandatory_Fields as e:
                    log.logger.warning(e.return_message())
                    return e.return_message()

            elif (self.password_validation(password,confirm_password)==True) and (self.email_validation(email_id)==True) and (self.contact_details_validation(phone_num)==True) and (self.checking_password(password) == True) and (self.age_validation(age)==True):
                if role == "Buyer":
                    ob_dto.set_values_buyer(user_name, age, email_id, password, confirm_password,phone_num, address, role)
                    result=ob_dao.signup_details_buyer()
                    return result
                elif role == "Seller":
                    addhar = request_data['Aadhar']
                    if self.aadhar_validation(addhar) == True:
                        ob_dto.set_values_seller(user_name, age, email_id, password, confirm_password, phone_num, address,  role, addhar)
                        result = ob_dao.signup_details_seller()
                        return result
                    else :
                        try:
                            raise exceptions.Aadhar_Invalid()
                        except exceptions.Aadhar_Invalid as e:
                            return e.return_message()
            elif(self.password_validation(password,confirm_password)==False):
                try:
                    raise exceptions.Password_mismatch()
                except exceptions.Password_mismatch as e:
                    log.logger.warning(e.return_message())
                    return e.return_message()
            elif (self.email_validation(email_id) == False):
                try:
                    raise exceptions.Email_Id_Invalid()
                except exceptions.Email_Id_Invalid as e:
                    log.logger.warning(e.return_message())
                    return e.return_message()
            elif (self.contact_details_validation(phone_num) == False):
                try:
                    raise exceptions.Phone_Number_Invalid()
                except exceptions.Phone_Number_Invalid as e:
                    log.logger.warning(e.return_message())
                    return e.return_message()
            elif (self.checking_password(password) == False):
                try:
                    raise exceptions.Invalid_Password()
                except exceptions.Invalid_Password as e:
                    log.logger.warning(e.return_message())
                    return e.return_message()
                    
            elif (self.age_validation(age)==False):
                try:
                    raise exceptions.Age_Invalid()
                except exceptions.Age_Invalid as e:
                    log.logger.warning(e.return_message())
                    return e.return_message()



    def login_details_emailid(self,email_id,password):
        '''
        login details of the user
        :param email_id: email Id of the user(String)
        :param password: Password of the user(String)
        :return: response message whether logged in or not
        '''
        log.logger.info("In login function in service layer")
        ob_dao = DaoUser.DaoImpl()
        ob_dto = login_dto.login_dto()
        if self.email_validation(email_id) == True:
            ob_dto.set_values(email_id,password)
            result = ob_dao.login_details_emailid()
            return result
        elif (self.email_validation(email_id) == False):
            try:
                raise exceptions.Email_Id_Invalid()
            except exceptions.Email_Id_Invalid as e:
                log.logging.warning(e.return_message())
                return e.return_message()


    def changing_password(self,uemail, num, password):
        """
        This method takes in email,phone number and password from the controller class and validates it,
        If validate it sets its value to the dto class and calls the dao class where the data is added to
        the database.
        :param password: 8-16 length string with atleast one uppercase and special character.
        :param num: phone number of length 10
        :return: If validated values are transfered to dao class else error message is printed
        """
        log.logger.info("In changing_password function in service layer")
        ob_dao = DaoUser.DaoImpl()
        ob_dto = change_password_dto.dto_forgot()
        if(self.checking_password(password)== True):
            ob_dto.set_values(uemail, num, password)
            x = ob_dao.changing_password()
            if x == "Invalid":
                try:
                    raise (exceptions.Email_id_not_present())
                except exceptions.Email_id_not_present as exp:
                    return exp.return_message()
            elif x == "InvalidNumber":
                try:
                    raise (exceptions.Wrong_phone_number())
                except exceptions.Wrong_phone_number as exp:
                    return exp.return_message()
            else:
                return x
        elif(self.checking_password(password)==False):
            try:
                raise (exceptions.Invalid_Password())
            except exceptions.Invalid_Password as exp:
                return exp.return_message()
        else:
            try:
                raise (exceptions.Invalid_number())
            except exceptions.Invalid_number as exp:
                return exp.return_message()


    def pymongo_exception(self):
        try:
            raise exceptions.Pymongo_Error()
        except exceptions.Pymongo_Error as e:
            log.logger.warning(e.return_message())
            return e.return_message()



