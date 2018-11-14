from DBUtil.dbutil import *#importing database layer
from DAO import DaoInterface#importing dao interface layer
from interface import implements#importing interface
from DTO import updateDTO#importing dto layer
from LogConfig import log_file as log#importing log configuration layer

class Dao_Update(implements(DaoInterface.DaoInterfaceUpdate)):
    def __init__(self):
        """
        self called constructor
        """
        pass

    def update_mail(self):
        """
        This method takes value from the dto class and sends the value to the database for updation
        :return: Updated if value is entered in the database
        """
        log.logger.info("In update_mail function of DaoUpdate layer")
        con = connect()
        ob_dto = updateDTO.Update_dto()
        (email_id,phone)= ob_dto.get_email()
        mycol = con["Users"]
        name = mycol.find_one({"Phone Number":phone})
        try:
            age = name['Age']
            mycol.update_one({"Phone Number": phone}, {"$set": {"Email_Id": email_id}})
            return "Profile updated successfully"
        except TypeError as t:
            return "Invalid"


    def update_num(self):
        """
        This method takes value from the dto class and sends the value to the database for updation
        :return: Updated if value is entered in the database
        """
        log.logger.info("In update_num function of DaoUpdate layer")
        con = connect()
        ob_dto = updateDTO.Update_dto()
        (email_id,phone)= ob_dto.get_email()
        mycol = con["Users"]
        name = mycol.find_one({"Email_Id":email_id})
        try:
            age = name['Age']
            mycol.update_one({"Email_Id":email_id}, {"$set": {"Phone Number": phone}})
            return "Profile updated successfully"
        except TypeError as t:
            return "Invalid"


    def update_address_dao(self):

        """
        This method takes value from the dto class and updates the address of the user in the database
        :return: Updated if value is entered in the database
        """
        log.logger.info("In update_address_dao function of DaoUpdate layer")
        con = connect()
        ob_dto = updateDTO.Update_dto()
        (email,address)= ob_dto.get_address()
        mycol = con["Users"]
        name = mycol.find_one({"Email_Id": email})
        try:
            age = name['Age']
            mycol.update_one({"Email_Id": email}, {"$set": {"Address": address}})
            return "Profile updated successfully"
        except TypeError as t:
            return "Mail Id not present"


    def check_password(self):
        """
        This method takes value from the dto class and checks if the email id provide exists in the database
        :return: "Mail Id not present" if email id is not present in the database, True if it is in the database
        """
        log.logger.info("In check_password function of DaoUpdate layer")
        con = connect()
        ob_dto = updateDTO.Update_dto()
        (email, password) = ob_dto.get_old_password()
        mycol = con["Users"]
        name = mycol.find_one({"Email_Id": email})
        try:
            if name['Password'] == password:
                return True
            else:
                return False
        except TypeError as t:
            return "Mail Id not present"


    def change_password(self):
        """
        After checking if the user is present in the database this method will update the existing password to the new password.
        :return:Profile updated successfully: if password is changed in the database,"Mail Id not present": if the id is not in the database
        """
        log.logger.info("In change_password function of DaoUpdate layer")
        con = connect()
        ob_dto = updateDTO.Update_dto()
        (email, password) = ob_dto.get_new_password()
        mycol = con["Users"]
        name = mycol.find_one({"Email_Id": email})
        try:
            age = name['Age']
            mycol.update_one({"Email_Id": email}, {"$set": {"Password": password}})
            return "Profile updated successfully"
        except TypeError as t:
            return "Mail Id not present"



    def display_dao(self):
        """
        This method is used to display all the books present in database to the front end.
        :return: List containing details of the books (Name,Price,Author,Define)
        """
        log.logger.info("In display_dao function of DaoUpdate layer")
        con = connect()
        display_list= []
        mycol = con["Books"]
        inner_list =[]
        for key in mycol.find():
            name = key["Name"]
            price = key["Price"]
            author = key["Author"]
            define = key["Define"]
            inner_list.append(name)
            inner_list.append(price)
            inner_list.append(author)
            inner_list.append(define)
            display_list.append(inner_list)
            inner_list=[]

        return display_list