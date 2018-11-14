from interface import Interface#importing interface

class ServiceOrderInterface(Interface):

    def add_to_wishlist(self, request_data):
        """
        :param request_data: adding books to wishlist
        :return: none
        """
        pass

    def display_details(self, data):
        """
        :param data: display book details
        :return: none
        """
        pass


class ServiceAdminInterface(Interface):
    def check_isbn(self, isbn):
        """
        :param isbn: checking valid isbn
        :return: none
        """
        pass

    def check_book(self,data):
        '''
        :param data: checking that the book is already present or not
        :return: none
        '''
        pass
    def add_books(self,request_data):
        '''
        :param request_data: adding details of book
        :return: none
        '''
        pass
    def delete_books(self,request_data):
        '''
        :param request_data: deleting the specific book
        :return: none
        '''
        pass


class ServiceInterfaceUpdate(Interface):
    def update_email(self, request_data):
        '''
        :param request_data: updating email of buyer
        :return: none
        '''
        pass

    def update_phone(self, request_data):
        '''
        :param request_data: updating phone number of buyer
        :return: none
        '''
        pass

    def update_address_service(self, data):
        '''
        :param data: updating address of buyer
        :return: none
        '''
        pass

    def update_password_service(self, data):
        '''
        :param data: updating password of buyer
        :return: none
        '''
        pass



class ServiceInterface(Interface):

    def signup_detail(self,request_data):
        '''
        :param request_data: json object - user signup details
        :return: none
        '''
        pass

    def login_details_emailid(self,email_id,password):
        '''
        :param email_id: user Email Id (abc@gmail.com)
        :param password: user Password (Abc@123456)
        :return: none
        '''
        pass

    def changing_password(self,uemail, num, password):
        """
        implemented in Service implementation
        """
        pass


		
class ServiceInterfaceSeller(Interface):
   def show_books(self, request_data):
       '''
       :param request_data: displaying book details
       :return: none
       '''
       pass
   def seller_add_books(self, request_data):
       '''
       :param request_data: adding book details to the seller database
       :return: none
       '''
       pass
   def seller_update_books(self, request_data):
       '''
       :param request_data: updating book details in the seller stock
       :return: none
       '''
       pass



