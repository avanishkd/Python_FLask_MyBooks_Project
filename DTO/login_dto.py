class login_dto():
    '''
    DTO Layer for Login
    '''
    __email_id = ""
    __password = ""

    def __init__(self):
        '''
        constructor called automatically
        '''
        pass

    def set_values(self,email_id,password):
        '''
        passing the required values for login
        :param email_id: String(email Id of the user)
        :param password: String(Password of the user)
        '''
        login_dto.__email_id = email_id
        login_dto.__password = password


    def get_values(self):
        '''
        Getting the values email Id and password
        :return: email ID and password
        '''
        return (login_dto.__email_id, login_dto.__password)