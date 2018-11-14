from DBUtil.dbutil import *#importing database layer
from DAO import DaoInterface#importing DaoInterface layer
from interface import implements#importing interface
from Service import ServiceAdmin#importing service admin layer
from DTO import add_books_dto,del_books_dto#importing dto layer
from LogConfig import log_file as log#importing log configuration layer

class Dao_impl_admin(implements(DaoInterface.Dao_interface_admin)):
    def add_books(self):
        '''
            Add the books to the book database by the admin
            :return: response from the database
        '''
        log.logger.info("In add_books function of DaoAdmin layer")
        ob_dto =add_books_dto.add_books_dto()
        con = connect()
        (isbn, name,publisher, author, price, type, define) = ob_dto.get_values()
        mycol = con["Books"]
        mydict = [{"_id": isbn,"Name":name, "Publisher": publisher, "Author": author, "Price": price,"Type": type, "Define": define}]
        mycol.insert_many(mydict)
        return "Successfully added"


    def delete_books(self):

        '''
            Delete the books from the book database by the admin
            :return: response from the database
        '''
        ob_dto = del_books_dto.del_books_dto()
        con = connect()
        (isbn) = ob_dto.get_values()
        mycol = con["Books"]
        isbn = mycol.find_one({"ISBN": isbn})
        sev_obj = ServiceAdmin.Service_impl_admin()
        res = sev_obj.check_book(isbn)
        if res == True:
            return "Not Available in database"
        else:
            mycol.delete_one(isbn)
            return "Deleted Successfully"
