from DBUtil.dbutil import *#importing database layer
from DAO import DaoInterface#importing dao interface layer
from interface import implements#importing interface
from DTO import signup_dto,add_books_dto#importing dto layer
from LogConfig import log_file as log#importing log configuration layer

class DaoImpl_Seller(implements(DaoInterface.Dao_interface_seller)):
    def __init__(self):
        '''
        constructor called automatically
        '''
        pass

    def show_books(self):
        '''
            this method displays the list in the book database to the seller
            :return: response whether displayed or not
        '''
        log.logger.info("In show_books function of DaoSeller layer")
        result = {}
        ob_dto_email_id = signup_dto.signup_dto()
        email_id = ob_dto_email_id.get_values_email()
        con = connect()
        mycol = con["Books"]
        mycol_2 = con["Seller"]
        find_email = mycol_2.find_one({"Email_Id":email_id})
        try:
            email = find_email["Email_Id"]
            if email == email_id:
                find_list = mycol.find({}, {"Name": 1, "Price": 1})
                for itr in find_list:
                    result[itr["Name"]] = itr["Price"]
                return result
            else:
                return "Invalid"
        except TypeError as E:
            return "Invalid Email ID"


    def seller_add_books(self):

        '''
            Add books to the seller database by the seller
            :return: response whether added or not
        '''
        log.logger.info("In seller_add_books function of DaoSeller layer")
        ob_dto_email_id = signup_dto.signup_dto()
        email_id = ob_dto_email_id.get_values_email()
        ob_dto = add_books_dto.add_books_dto()
        (book_name,book_price) = ob_dto.get_values_books()
        con = connect()
        mycol = con["Books"]
        mycol_2 = con["Seller"]
        find_books = mycol.find_one({"Name":book_name})
        try:
            bookname = find_books["Name"]
            if bookname == book_name:
                try:
                    find_email = mycol_2.find_one({"Email_Id":email_id},{"_id":0,"Email_Id":1})
                    find_email_id = mycol_2.find_one({"Email_Id":email_id,"BookList":{"$elemMatch":{"BookName":bookname}}},{"_id":0,"Email_Id":1})
                    if find_email["Email_Id"] == email_id:
                        try:
                            find_book = mycol_2.find_one({"Email_Id": email_id, "BookList": {"$elemMatch": {"BookName": bookname}}},{"_id": 0, "BookList": 1})
                            book_present = find_book['BookList']
                            return "Book Already Present, Updated existing"
                        except TypeError as e:
                            mycol_2.update({"Email_Id": email_id}, {"$addToSet": {"BookList": {"BookName": book_name,"BookNum":1,"BookCost": book_price}}})
                            return "Added to the Seller database"
                except TypeError as e:
                    return "Invalid Seller Email Id"
        except TypeError as E:
            return "Invalid Book"


    def seller_update_books(self):

        '''
            Updating books in the seller stock by the seller
            :return: response whether updated or not
        '''
        log.logger.info("In seller_update_books function of DaoSeller layer")
        ob_dto_email_id = signup_dto.signup_dto()
        email_id = ob_dto_email_id.get_values_email()
        ob_dto = add_books_dto.add_books_dto()
        (book_name, book_num) = ob_dto.get_values_update_books()
        con = connect()
        mycol = con["Books"]
        mycol_2 = con["Seller"]
        try:
            find_email = mycol_2.find_one({"Email_Id": email_id}, {"_id": 0, "Email_Id": 1})
            if find_email["Email_Id"] == email_id:
                try:
                    find_book = mycol_2.find_one({"Email_Id": email_id, "BookList": {"$elemMatch": {"BookName": book_name}}},{"_id": 0, "BookList": {"$elemMatch": {"BookName": book_name}}})
                    books = (find_book["BookList"])
                    num_of_books = books[0]["BookNum"]
                    if num_of_books == 0 and int(book_num) < 0:
                        return "No Books Available"
                    else:
                        number_book = int(book_num) + num_of_books
                        mycol_2.update({"Email_Id": email_id, "BookList.BookName": book_name},{"$set": {"BookList.$.BookNum": number_book}})
                        return "Updated"
                except TypeError as E:
                    return "Invalid Bookname"
        except TypeError as E:
            return "Invalid Seller Email Id"

