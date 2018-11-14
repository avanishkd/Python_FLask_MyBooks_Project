from DBUtil.dbutil import *#importing database layer
from DAO import DaoInterface#importing DaoInterface layer
from interface import implements#importing interface
from Service import ServiceUser#importing service user layer
from DTO import OrderDto,wish_dto#importing dto layer
from LogConfig import log_file as log#importing log configuration layer


class Dao_Orders(implements(DaoInterface.Dao_Interface_Order)):
    """
    Dao orders class is used to keep all the functions related to order part of the user.
    """
    def check_book_wishlist(self,book_id,user_id):
        con = connect()
        mycol = con["Wishlist"]
        log.logger.info("Working")
        try:
            book_detail = mycol.find_one({"User": user_id})
            wish_user = book_detail["User"]
            log.logger.info(book_id)
            try:
                wish_detail = mycol.find_one({"$and": [{"User": user_id}, {"BookList": {"$elemMatch": {"ISBN": book_id}}}]})
                wish_book = wish_detail["User"]
                return "Book Already Present"
            except TypeError as t:
                try:
                    mycol.update({"User": user_id}, {"$push": {"BookList": {"ISBN": book_id}}})
                    return "Added to wishlist successfully"
                except Exception as e:
                    service = ServiceUser.ServiceImpl()
                    service.pymongo_exception()
        except TypeError as e:
            return "First Book"


    def display_wishlist_dao(self,user_id):
        """
        this method displays all the books present in the wishlist of the user.
        :param user_id: The email id of the user logged in
        :return: A variable having list of all the books in the wishlist of the user
        """
        con = connect()
        mycol = con["Wishlist"]
        details = mycol.find_one({"User":user_id})
        var = details['BookList']
        return var



    def add_to_wishlist(self):
        """
                This method takes value from the dto class and adds it to the wishlist of the user
                :return: Updated if value is entered in the database
        """
        ob_dto_wish = wish_dto.Wish_Dto()
        (book_id,email_id)=ob_dto_wish.get_wish()
        try:
            log.logger.info("In add to wishlist in function")
            con = connect()
            mycol = con["Wishlist"]
            try:
                mycol.insert({"User": email_id, "BookList": [{"ISBN": book_id}]})
                return "Added to wishlist successfully"
            except Exception as e:
                self.service.pymongo_exception()
        except Exception as E:
            print(E)



    def check_book_num(self):
        """
        This methods checks the number of books present with the seller before assigning the seller with any order
        :return: True if the number of books is more than 2 else False
        """
        log.logger.info("In check book num function of Dao Order layer")
        ob_dto = OrderDto.Order_Dto()
        (book_id, seller_id, user_id) = ob_dto.get_cart()
        con = connect()
        mycol = con["Books"]
        book_details = mycol.find_one({"ISBN": book_id})
        book_name = book_details["Name"]
        mycol2 = con["Seller"]
        seller = mycol2.find_one({"BookList":{"$elemMatch":{"BookName":book_name}}},{"_id":0,"BookList":1})
        count = seller['BookList'][0]['BookNum']
        print(count)
        if count < 2:
            return False
        else:
            return True



    def adding_to_cart(self):
        """
        This methods adds books to the cart of the user
        :return: success message if values is added to the cart
        """
        log.logger.info("In adding_to_cart function of Dao Order layer")
        ob_dto = OrderDto.Order_Dto()
        (book_id,seller_id,user_id) = ob_dto.get_cart()
        con = connect()
        mycol = con["Cart"]
        mycol.insert(({"user":user_id,"cart":[{book_id:seller_id}]}))
        return "Added to the cart"


    def display(self):
        """
        This methods is used to display the details of each book with their name price and details.
        :return: book details
        """
        log.logger.info("In display function of Dao Order layer")
        ob_dto = OrderDto.Order_Dto()
        book_id= ob_dto.get_bookId()
        con = connect()
        mycol = con["Books"]
        mycol2 = con["Seller"]
        book_details = mycol.find_one({"ISBN" : book_id})
        book_name = book_details["Name"]
        list_book = []
        list_book.append(book_name)
        list_book.append(book_details["Define"])
        list_book.append(book_details["Price"])
        list_seller =[]
        itr =0
        for x in mycol2.find({"BookList":{"$elemMatch":{"BookName":book_name}}},{"_id":0,"BookList":1,"Username":1}):
            list_seller.append(x["Username"])
            list_seller.append(x['BookList'][0]['BookCost'])
            itr = itr+1
        return  (list_book,list_seller)

    def get_seller(self,book_id):
        '''
        :param book_id: isbn
        :return: list of sellers in the seller database
        '''
        log.logger.info("In order_dao function of Dao Order layer")
        ob_dto = OrderDto.Order_Dto()
        book_id = ob_dto.get_order()
        con = connect()
        mycol = con["Seller"]
        max_num=0
        min_cost=500
        best_seller="None"
        try:
            for value in mycol.find():
                print(value["Email_Id"])
                seller_id = value["Email_Id"]
                seller_book = mycol.find_one({"Email_Id":seller_id},{"BookList":{ "$elemMatch":{"BookName" : "Harry Potter"}}})
                try:
                    temp_var = seller_book['BookList']
                    book_num = seller_book['BookList']['BookNum']
                    book_cost = seller_book['BookList']['BookCost']
                    if book_num>max_num:
                        max_num=book_num
                    if book_cost<min_cost:
                        min_cost=book_cost
                        best_seller = seller_id
                except KeyError as e:
                    continue
            return best_seller
        except TypeError as e:
            return best_seller

    def order_book_dao(self,user_id):
        '''
        :param user_id: email id
        :return: response message whether ordered or not
        '''
        log.logger.info("In order_dao function of Dao Order layer")
        ob_dto = OrderDto.Order_Dto()
        book_id = ob_dto.get_order()
        con = connect()
        seller_email="aditya21@gmail.com"
        mycol = con["Order"]
        try:
            order_detail = mycol.find_one({"user": user_id})
            temp = order_detail['user']
            mycol.update_one({"user": user_id},{"$push": {"cart": {"ISBN": book_id,"seller_id":seller_email}}})
            return "Order Placed"
        except TypeError as e:
            try:
                mycol.insert(({"user": user_id, "cart": [{"ISBN": book_id,"seller_id":seller_email}]}))
                return "Order Placed"
            except Exception as e:
                service_obj=ServiceUser.ServiceImpl()
                service_obj.pymongo_exception()




