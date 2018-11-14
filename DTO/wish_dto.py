class Wish_Dto():
    """
    DTO layer of Wishlist
    """
    __book_Id = ""
    __user_id =""

    def set_wish(self,book_id,user_id):
        """
         passing the required fields for wishlist method
        :param book_id:
        :param user_id:
        """
        Wish_Dto.__book_Id=book_id
        Wish_Dto.__user_id=user_id

    def get_wish(self):
        """
         Extracting the values passed from dao layer of wishlist
        :return: book id(isbn), user id(email id)
        """
        return (Wish_Dto.__book_Id,Wish_Dto.__user_id)
