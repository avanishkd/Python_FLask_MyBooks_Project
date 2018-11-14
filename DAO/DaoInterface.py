from interface import Interface#importing interface

class Dao_Interface_Order(Interface):
    def add_to_wishlist(self):
        '''
            add books to wishlist
        '''
        pass

    def check_book_wishlist(self, book_id, user_id):
        '''
            checks whether the book is already present in the wishlist or not
        '''
        pass

    def display(self):
        '''
            display the books of a particular seller
        '''
        pass


class Dao_interface_admin(Interface):
    def add_books(self):
        '''
        add the book details
        '''
        pass
    def delete_books(self):
        '''
        delete the book
        '''
        pass


class DaoInterfaceUpdate(Interface):
    def update_num(self):
        '''
            updating the phone number of user
        '''
        pass

    def update_mail(self):
        '''
            updating the email id of user
        '''
        pass

    def update_address_dao(self):
        '''
            updating the address of user
        '''
        pass

    def change_password(self):
        '''
            updating the password of user
        '''
        pass


class DaoInterface(Interface):

    def signup_details_buyer(self):
        '''
        signup details of buyer
        '''
        pass

    def signup_details_seller(self):
        '''
        signup details of seller
        '''
        pass

    def login_details_emailid(self):
        '''
        signup details of user
        '''
        pass

    def changing_password(self):
        """
        implemented in dao implementation
        """
        pass


		
class Dao_interface_seller(Interface):
    def show_books(self):
        '''
        display the book details to the seller
        '''
        pass

    def seller_add_books(self):
        '''
        add books by the seller
        '''
        pass

    def seller_update_books(self):
        '''
        update the books in the seller stock
        '''
        pass







