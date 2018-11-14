class Update_dto():
    """
    DTO of layer of updation
    """
    __email = ''
    __phone = ''
    __address=''
    __old_password=''
    __new_password = ''

    def __init__(self):
        '''
        constructor called automatically
        '''
        pass

    def set_email(self,mail,phone):
        """
        passing the required fields for updating email id of buyer
        :param mail:
        :param phone:
        """
        Update_dto.__email = mail
        Update_dto.__phone=phone

    def get_email(self):
        """
         Extracting the values passed from dao layer of updation
        :return: email id, phone number
        """
        return (Update_dto.__email,Update_dto.__phone)

    def set_address(self,email,address):
        """
        passing the required fields for updating address of buyer
        :param email:
        :param address:
        """
        Update_dto.__email=email
        Update_dto.__address = address

    def get_address(self):
        """
         Extracting the values passed from dao layer of updation
        :return: email id , address
        """
        return (Update_dto.__email,Update_dto.__address)

    def set_old_password(self,email,password):
        """
        passing the required fields for updating old password of buyer
        :param email:
        :param password:
        """
        Update_dto.__email =email
        Update_dto.__old_password = password

    def get_old_password(self):
        """
         Extracting the values passed from dao layer of updation
        :return: email id , old password
        """
        return (Update_dto.__email,Update_dto.__old_password)

    def set_new_password(self,password):
        """
        passing the required fields for updating new password of buyer
        :param password:
        """
        Update_dto.__new_password=password

    def get_new_password(self):
        """
         Extracting the values passed from dao layer of updation
        :return: email id , new password
        """
        return (Update_dto.__email,Update_dto.__new_password)

