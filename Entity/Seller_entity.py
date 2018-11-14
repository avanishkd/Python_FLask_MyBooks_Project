class Seller():
    '''
    Entity class for seller
    '''
    __email_id = ""
    __feedback = []
    __booklist = []
    __rating = ""

    def __init__(self):
        pass

    def set_values(self,email_id,feedback,booklist,rating):
        Seller.__email_id = email_id
        Seller.__feedback.append(feedback)
        Seller.__booklist.append(booklist)
        Seller.__rating = rating


    def get_values(self):
        return (Seller.__email_id, Seller.__feedback, Seller.__booklist, Seller.__rating)