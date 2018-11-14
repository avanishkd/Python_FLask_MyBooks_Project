from DAO import DaoSeller#importing dao seller layer
from Service import ServiceInterface#importing service interface layer
from interface import implements#importing interface
from Exceptions import exceptions#importing exceptions layer
from DTO import signup_dto,add_books_dto#importing dto layer
from LogConfig import log_file as log#importing log configuration layer

class Service_impl_Seller(implements(ServiceInterface.ServiceInterfaceSeller)):

    def __init__(self):
        '''
        contructor called automatically
        '''
        pass

    def show_books(self, request_data):
        '''
        display the list of books in the book database to the seller
        :param request_data: json object containing email id of seller
        :return: displayed or not
        '''
        log.logger.info("In show_books function of ServiceSeller layer")
        ob_dao = DaoSeller.DaoImpl_Seller()
        ob_dto_email_id = signup_dto.signup_dto()
        email_id = request_data["Email_Id"]
        ob_dto_email_id.set_values_email(email_id)
        result = ob_dao.show_books()
        if result == "Invalid Email ID":
            try:
                raise exceptions.Email_Check()
            except exceptions.Email_Check as e:
                return e.return_message()
        else:
            return result


    def seller_add_books(self, request_data):
        '''
        add the books to the seller stock by the seller
        :param request_data: json object containing book details
        :return: added or not
        '''
        log.logger.info("In seller_add_books function of ServiceSeller layer")
        ob_dao = DaoSeller.DaoImpl_Seller()
        ob_dto = add_books_dto.add_books_dto()
        ob_dto_email_id = signup_dto.signup_dto()
        email_id = request_data["Email_Id"]
        book_name = request_data["Name"]
        book_price = request_data["Price"]
        ob_dto_email_id.set_values_email(email_id)
        ob_dto.set_values_books(book_name,book_price)
        result = ob_dao.seller_add_books()
        if result == "Invalid Seller Email Id":
            try:
                raise exceptions.Seller_Email_check()
            except exceptions.Seller_Email_check as e:
                return e.return_message()
        elif result == "Invalid Book":
            try:
                raise exceptions.Bookname_check()
            except exceptions.Bookname_check as e:
                return e.return_message()
        else:
            return result


    def seller_update_books(self, request_data):
        '''
        updating book details in the seller database by the seller
        :param request_data: json object containing book details
        :return: updated or not
        '''
        log.logger.info("In seller_update_books function of ServiceSeller layer")
        ob_dao = DaoSeller.DaoImpl_Seller()
        ob_dto = add_books_dto.add_books_dto()
        ob_dto_email_id = signup_dto.signup_dto()
        email_id = request_data["Email_Id"]
        book_name = request_data["Name"]
        book_num = request_data["BookNum"]
        ob_dto_email_id.set_values_email(email_id)
        ob_dto.set_values_update_books(book_name,book_num)
        result = ob_dao.seller_update_books()
        if result == "Invalid Seller Email Id":
            try:
                raise exceptions.Seller_Email_check()
            except exceptions.Seller_Email_check as e:
                return e.return_message()
        elif result == "Invalid Bookname":
            try:
                raise exceptions.Bookname_check()
            except exceptions.Bookname_check as e:
                return e.return_message()
        elif result == "No Books Available":
            try:
                raise exceptions.Book_Count()
            except exceptions.Book_Count as e:
                return e.return_message()
        else:
            return result


