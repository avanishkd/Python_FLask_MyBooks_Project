from DAO import DaoOrder#importing dao order layer
from Service import ServiceInterface#importing service interface layer
from interface import implements#importing interface
from DTO import login_dto,OrderDto,wish_dto#importing dto layer
from LogConfig import log_file as log#importing log configuration layer

class Service_Order(implements(ServiceInterface.ServiceOrderInterface)):
    def add_to_wishlist(self, request_data):

        """
        Adding book to the wishlist of a particular buyer
        :param request_data: json object
        :return:response from the database after validating all the fields
        """
        log.logger.info("In add to wishlist function in service layer")
        ob_dao = DaoOrder.Dao_Orders()
        ob_login_dto = login_dto.login_dto()
        book_id = request_data['ISBN']
        (user_id,password) = ob_login_dto.get_values()
        obj_dto = wish_dto.Wish_Dto()
        obj_dto.set_wish(book_id,user_id)
        check_book = ob_dao.check_book_wishlist(book_id,user_id)
        if check_book == "First Book":
            result=ob_dao.add_to_wishlist()
            return result
        else:
            return check_book


    def display_wishlist_service(self):
        '''
        This method display the book details which were added to the wishlist of a particular buyer
        :return: response message
        '''
        log.logger.info("In display wishlist function in service layer")
        ob_login_dto = login_dto.login_dto()
        ob_dao = DaoOrder.Dao_Orders()
        (user_id, password) = ob_login_dto.get_values()
        result = ob_dao.display_wishlist_dao(user_id)
        return result


    def add_to_cart_service(self,data):
        """
        Adding the books to the cart of particular buyer
        :param data: seller id , user id
        :return:response message whether added or not
        """
        log.logger.info("In add to cart function in service layer")
        seller_id = data['Seller_Id']
        user_id = data['User_Id']
        obj_dto = OrderDto.Order_Dto()
        ob_dao = DaoOrder.Dao_Orders()
        obj_dto.set_cart(seller_id,user_id)
        result = ob_dao.check_book_num()
        if result == True:
            res = ob_dao.adding_to_cart()
            return res
        else:
            return "Unable to add"


    def display_details(self,data):
        """
        This method displays the book details
        :param data: book id
        :return: book details
        """
        log.logger.info("In diaplay_details function of service layer")
        obj_dto = OrderDto.Order_Dto()
        book_id = data['book_id']
        obj_dto.set_bookID(book_id)
        ob_dao = DaoOrder.Dao_Orders()
        res = ob_dao.display()
        return res


    def order_book_service(self,data):
        '''
        :param data: book id
        :return: response message whether ordered or not
        '''
        log.logger.info("In order_service function of service layer")
        obj_dto = OrderDto.Order_Dto()
        book_id = data['ISBN']
        obj_dto.set_order(book_id)
        ob_dao = DaoOrder.Dao_Orders()
        ob_login_dto = login_dto.login_dto()
        (user_id, password) = ob_login_dto.get_values()
        # seller_id= ob_dao.get_seller(book_id)
        # print(seller_id)
        result = ob_dao.order_book_dao(user_id)
        return result


