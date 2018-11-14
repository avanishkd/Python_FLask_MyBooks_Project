class Order_Dto():
    """
    DTO layer of Order
    """
    __book_Id = ""
    __seller_id = ""
    __user_id = ""

    def set_bookID(self,book_id):
        """
         passing the required fields for add to wishlist method
        :param book_id:
        """
        Order_Dto.__book_Id=book_id

    def get_bookId(self):
        """
        Extracting the values passed from dao layer of add to wishlist
        :return: book id(isbn)
        """
        return Order_Dto.__book_Id

    def set_cart(self,seller_id,user_id):
        """
        passing the required fields for add to cart method
        :param seller_id:
        :param user_id:
        """
        Order_Dto.__seller_id = seller_id
        Order_Dto.__user_id = user_id

    def get_cart(self):
        """
        Extracting the values passed from dao layer of add to cart
        :return: book id(isbn), seller id(seller email id), user id(buyer email id)
        """
        return (Order_Dto.__book_Id,Order_Dto.__seller_id,Order_Dto.__user_id)

    def set_order(self,book_id):
        """
        passing the required fields for ordering
        :param book_id:
        """
        Order_Dto.__book_Id =book_id

    def get_order(self):
        """
        Extracting the values passed from dao layer of order
        :return: book id(isbn)
        """
        return (Order_Dto.__book_Id)