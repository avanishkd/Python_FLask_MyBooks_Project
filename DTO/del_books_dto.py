class del_books_dto():
    '''
    DTO Layer for Deleting Books
    '''
    __isbn = ""

    def __init__(self):
        '''
        constructor called automatically
        '''
        pass

    def set_values(self,isbn):
        """
        passing the required values for deleting books
        :param isbn:
        """
        del_books_dto.__isbn = isbn


    def get_values(self):
        '''
        Getting the values email Id and password
        :return: isbn
        '''
        return (del_books_dto.__isbn)