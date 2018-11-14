class Buyer():
    '''
    Entity class for buyer
    '''

    __user_name = ""
    __age = ""
    __email_id = ""
    __password = ""
    __confirm_password = ""
    __phone_num = ""
    __address = ""
    __preferences = []
    __role = ""

    def __init__(self):
        pass

    def set_values(self,user_name,age,email_id,password,confirm_password,phone_num,address,preferences,role):
        Buyer.__user_name = user_name
        Buyer.__age = age
        Buyer.__email_id = email_id
        Buyer.__password = password
        Buyer.__confirm_password = confirm_password
        Buyer.__phone_num = phone_num
        Buyer.__address = address
        Buyer.__preferences.append(preferences)
        Buyer.__role = role


    def get_values(self):
        return (Buyer.__user_name, Buyer.__age, Buyer.__email_id, Buyer.__password, Buyer.__confirm_password, Buyer.__phone_num, Buyer.__address, Buyer.__preferences, Buyer.__role)

