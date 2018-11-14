class add_books_dto():
    '''
    DTO Layer for adding books by admin
    '''
    __book_isbn=""
    __book_name=""
    __book_publisher=""
    __book_author=""
    __book_price=""
    __book_type=""
    __book_define=""
    __book_num = ""

    def __init__(self):
        pass

    def set_values(self,book_isbn,book_name,book_publisher,book_author,book_price,book_type,book_define):
        """
        passing the required fields for adding books in the book database
        :param book_isbn:
        :param book_name:
        :param book_publisher:
        :param book_author:
        :param book_price:
        :param book_type:
        :param book_define:
        """
        add_books_dto.__book_isbn=book_isbn
        add_books_dto.__book_name=book_name
        add_books_dto.__book_publisher=book_publisher
        add_books_dto.__book_author=book_author
        add_books_dto.__book_price=book_price
        add_books_dto.__book_type=book_type
        add_books_dto.__book_define=book_define

    def get_values(self):
        """
        Extracting the values passed from dao layer of admin add books
        :return: isbn, book name, book publisher, book author, book price, book type, book definition
        """
        return(add_books_dto.__book_isbn,add_books_dto.__book_name,add_books_dto.__book_publisher,add_books_dto.__book_author,add_books_dto.__book_price,add_books_dto.__book_type,add_books_dto.__book_define)


    def set_values_books(self,book_name,book_price):
        """
        passing the required fields for adding books in the book database
        :param book_name:
        :param book_price:
        """
        add_books_dto.__book_name = book_name
        add_books_dto.__book_price = book_price


    def get_values_books(self):
        """
        Extracting the values passed from dao layer of admin add books
        :return: book name , book price
        """
        return (add_books_dto.__book_name, add_books_dto.__book_price)

    def set_values_update_books(self,book_name,book_num):
        """
        passing the required fields for updating books in the book database
        :param book_name:
        :param book_num:
        """
        add_books_dto.__book_name = book_name
        add_books_dto.__book_num = book_num

    def get_values_update_books(self):
        """
        Extracting the values passed from dao layer of admin update books
        :return: book name , number of books
        """
        return (add_books_dto.__book_name, add_books_dto.__book_num)