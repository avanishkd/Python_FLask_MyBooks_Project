from DAO import DaoUpdate#importing dao update layer
from Service import ServiceInterface,ServiceUser#importing service interface layer
from interface import implements#importing interface
from Exceptions import exceptions#importing exceptions layer
from DTO import updateDTO#importing dto layer
from LogConfig import log_file as log#importing log configuration layer


class Service_Update(implements(ServiceInterface.ServiceInterfaceUpdate)):

    def __init__(self):
        '''
        contructor called automatically
        '''
        pass

    def update_email(self, request_data):

        """
               This method takes user profile entity values from the controller class and validates it,
               If validate it sets its value to the dto class and calls the dao class where the data is added to
               the database.
               :param request_data: json object
                :return:response from the database after validating all the fields
        """
        log.logger.info("In update profile function in service layer")
        service = ServiceUser.ServiceImpl()
        ob_dao = DaoUpdate.Dao_Update()
        ob_dto = updateDTO.Update_dto()
        email_id = request_data['Email_Id']
        phone_num = request_data['phone']
        print("Service ", phone_num)
        if (email_id == "" or phone_num == ""):
            try:
                raise exceptions.Mandatory_Fields()
            except exceptions.Mandatory_Fields as e:
                log.logger.warning(e.return_message())
                return e.return_message()
        elif (service.email_validation(email_id) == True and service.contact_details_validation(phone_num) == True):
            ob_dto.set_email(email_id, phone_num)
            result = ob_dao.update_mail()
            return result
        elif (service.contact_details_validation(phone_num) == False):
            try:
                raise exceptions.Phone_Number_Invalid()
            except exceptions.Phone_Number_Invalid as e:
                log.logger.warning(e.return_message())
                return e.return_message()

        elif (service.email_validation(email_id) == False):
            try:
                raise exceptions.Email_Id_Invalid()
            except exceptions.Email_Id_Invalid as e:
                log.logger.warning(e.return_message())
                return e.return_message()



    def update_phone(self, request_data):

        """
               This method takes user profile entity values from the controller class and validates it,
               If validate it sets its value to the dto class and calls the dao class where the data is added to
               the database.
               :param request_data: json object
                :return:response from the database after validating all the fields
        """

        service = ServiceUser.ServiceImpl()
        log.logger.info("In update profile function in service layer")
        ob_dao = DaoUpdate.Dao_Update()
        ob_dto = updateDTO.Update_dto()
        email_id = request_data['Email_Id']
        phone_num = request_data['phone']
        if (email_id == "" or phone_num == ""):
            try:
                raise exceptions.Mandatory_Fields()
            except exceptions.Mandatory_Fields as e:
                log.logger.warning(e.return_message())
                return e.return_message()
        elif (service.email_validation(email_id) == True and service.contact_details_validation(phone_num) == True):
            ob_dto.set_email(email_id, phone_num)
            result = ob_dao.update_num()
            return result
        elif (service.contact_details_validation(phone_num) == False):
            try:
                raise exceptions.Phone_Number_Invalid()
            except exceptions.Phone_Number_Invalid as e:
                log.logger.warning(e.return_message())
                return e.return_message()

        elif (service.email_validation(email_id) == False):
            try:
                raise exceptions.Email_Id_Invalid()
            except exceptions.Email_Id_Invalid as e:
                log.logger.warning(e.return_message())
                return e.return_message()



    def update_address_service(self,data):
        """
        Method to call dao layer to update address of the user
        :param request_data: json object
        :return: String with correct error or success message
        """
        log.logger.info("In update_address_service function of ServiceUpdate layer")
        ob_dao = DaoUpdate.Dao_Update()
        ob_dto = updateDTO.Update_dto()
        email = data['Email_Id']
        address = data['Address']
        if address == "":
            try:
                raise exceptions.Mandatory_Fields()
            except exceptions.Mandatory_Fields as e:
                return e.return_message()
        else:
            ob_dto.set_address(email, address)
            result = ob_dao.update_address_dao()
            return result



    def update_password_service(self,data):
        """
                Method to call dao layer to update address of the user
                :param request_data: json object
                :return: String with correct error or success message
        """
        log.logger.info("In update_password_service function of ServiceUpdate layer")
        ob_dao = DaoUpdate.Dao_Update()
        ob_dto = updateDTO.Update_dto()
        service = ServiceUser.ServiceImpl()
        email = data['Email_Id']
        old_pass = data['Password']
        new_pass = data['New_Password']
        ob_dto.set_old_password(email,old_pass)
        res = ob_dao.check_password()
        if (email == "" or old_pass == '' or new_pass==''):
            try:
                raise exceptions.Mandatory_Fields()
            except exceptions.Mandatory_Fields as e:
                return e.return_message()
        elif res:
            if service.checking_password(new_pass):
                ob_dto.set_new_password(new_pass)
                result = ob_dao.change_password()
                return result
            else:
                try:
                    raise exceptions.Invalid_Password()
                except exceptions.Invalid_Password as e:
                    return e.return_message()
        else:
            return "Password Incorrect"



    def display_service(self):
        """
        Service layer
        :return:
        """
        log.logger.info("In display_service function of ServiceUpdate layer")
        ob_dao = DaoUpdate.Dao_Update()
        result = ob_dao.display_dao()
        return result



