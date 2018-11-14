class dto_forgot():

    __phone_num = ''
    __new_pass = ''
    __email=''

    def __init__(self):
        '''
        constructor called automatically
        '''
        pass

    def set_values(self,uemail,num,password):
        """
        This method takes value from service layer and sets them to the class variables
        :param password: password value taken from service layer
        :param num: password value taken from service layer
        """
        dto_forgot.__email=uemail
        dto_forgot.__phone_num=num
        dto_forgot.__new_pass=password

    def get_values(self):
        """
        Method for returning value of class variables to the dao implementation class
        :return: Returns the value of class variables to the dao implementation class
        """
        return (dto_forgot.__email,dto_forgot.__phone_num,dto_forgot.__new_pass)
