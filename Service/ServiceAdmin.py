from DAO import DaoAdmin#importing dao admin layer
from Service import ServiceInterface#importing service inteface layer
from interface import implements#importing interface
from Exceptions import exceptions#importing exceptions layer
from DTO import add_books_dto,del_books_dto#importing dto layer
from LogConfig import log_file as log#importing log configuration layer


class Service_impl_admin(implements(ServiceInterface.ServiceAdminInterface)):

    def __init__(self):
        '''
        contructor called automatically
        '''
        pass

    def check_isbn(self,isbn):
        '''
        checking a book isbn valid or invalid
        :param isbn:
        :return: boolean either true or false
        '''
        log.logger.info("In check_isbn function of SellerAdmin layer")
        data = [itr for itr in isbn if itr in '0123456789Xx']
        if len(data) != 10: return False
        if data[-1] in 'Xx': data[-1] = 10
        try:
            return not sum((10 - i) * int(x) for i, x in enumerate(data)) % 11
        except ValueError:
            return False

    def check_book(self,data):
        '''
        checking whether the book is already present or not
        :param data: book isbn
        :return: true or error message
        '''
        log.logger.info("In check_book function of SellerAdmin layer")
        try:
            isbn = data["ISBN"]
            try:
                raise exceptions.Book_Already_Present()
            except exceptions.Book_Already_Present as e:
                return e.return_message()
        except TypeError as e:
            return True


    def add_books(self, request_data):
        '''
        adding books to the book database
        :param request_data: book details
        :return: response message whether added or not
        '''
        log.logger.info("In add_books function of SellerAdmin layer")
        ob_dao_admin=DaoAdmin.Dao_impl_admin()
        ob_dto = add_books_dto.add_books_dto()
        isbn= request_data['ISBN']
        name=request_data['Name']
        publisher = request_data['Publisher']
        author = request_data['Author']
        price = request_data['Price']
        type = request_data['Type']
        define = request_data['Define']
        ob_dto.set_values(isbn,name,publisher,author,price,type,define)
        if self.check_isbn(str(isbn))==True:
            res = ob_dao_admin.add_books()
            return res
        elif self.check_isbn(str(isbn))==False:
            try:
                raise exceptions.ISBN_not_correct()
            except exceptions.ISBN_not_correct as e:
                return e.return_message()


    def delete_books(self,request_data):
        '''
        deleting books in the book database
        :param request_data: book isbn
        :return: response message whether deleted or not
        '''
        ob_dao_admin = DaoAdmin.Dao_impl_admin()
        ob_dto = del_books_dto.del_books_dto()
        isbn = request_data['ISBN']
        ob_dto.set_values(isbn)
        if self.check_isbn(str(isbn)) == True:
            res = ob_dao_admin.delete_books()
            return res
        elif self.check_isbn(str(isbn)) == False:
            try:
                raise exceptions.ISBN_not_correct()
            except exceptions.ISBN_not_correct as e:
                return e.return_message()
