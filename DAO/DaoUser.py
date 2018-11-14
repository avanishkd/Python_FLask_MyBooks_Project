from DBUtil.dbutil import *#importing database layer
from DAO import DaoInterface#importing dao interface layer
from interface import implements#importing interface
from Service import ServiceUser#importing service user layer
from DTO import login_dto,signup_dto,change_password_dto#importing dto layer
from LogConfig import log_file as log#importing log configuration layer


class DaoImpl(implements(DaoInterface.DaoInterface)):
    def __init__(self):
        """
        self called constructor
        """
        pass


    def signup_details_buyer(self):
        '''
        Signup details of the buyer , updating in the database if not present
        :return: response from database whether updated or not
        '''
        ob_dto = signup_dto.signup_dto()
        log.logger.info("In sign up function for buyer")
        con=connect()
        (user_name,age,email_id,password,phone_num,address,role) = ob_dto.get_values_buyer()
        mycol = con["Users"]
        mydict = [{"Username": user_name,"Age":age,"Email_Id":email_id,"Password":password,"Phone Number":phone_num,"Address":address,"Role":role}]
        username = mycol.find_one({"Email_Id":email_id})
        service_obj = ServiceUser.ServiceImpl()
        res = service_obj.check_user(username)
        if res == "False":
            try:
                mycol.insert_many(mydict)
                log.logger.info("User details added to the database")
                return "Successfully added"
            except Exception as e:
                service_obj.pymongo_exception()
        else:
            return res


    def signup_details_seller(self):
        '''
        Signup details of the seller , updating in the database if not present
        :return: response from database whether updated or not
        '''
        ob_dto = signup_dto.signup_dto()
        log.logger.info("In sign up function for seller")
        con = connect()
        (user_name,age,email_id,password,phone_num,address,role,addhar_num) = ob_dto.get_values_seller()
        mycol = con["Seller"]
        mydict =[{"Username": user_name,"Age":age,"Email_Id":email_id,"Password":password,"Phone Number":phone_num,"Address":address,"Role":role,"Feedback":[],"BookList":[],"Rating":[],"Addhar_Num":addhar_num}]
        username = mycol.find_one({"Email_Id":email_id})
        service_obj = ServiceUser.ServiceImpl()
        res = service_obj.check_user(username)
        if res=="False":
            try:
                mycol.insert_many(mydict)
                log.logger.info("User details added to the database")
                return "Successfully added"
            except Exception as e:
                service_obj.pymongo_exception()
        else:
            return res



    def login_details_emailid(self):
        '''
        Login the user, if present in database
        :return: response from the database
        '''
        ob_dto = login_dto.login_dto()
        try:
            log.logger.info("In login in function")
            con = connect()
            (email_id,password) = ob_dto.get_values()
            mycol = con["Users"]
            res = mycol.find_one({"Email_Id": email_id})
            if res == None:
                mycol2 = con["Seller"]
                res2 = mycol2.find_one({"Email_Id": email_id})
                if res2 == None:
                    return "EmailId Not Registered"
                elif res2["Password"] == password:
                    log.logger.info("Logged In")
                    return "Logged In As Seller"
                else:
                    log.logger.info("Email Id and Password doesn't match")
                    return "Email Id  and Password doesn't match"
            elif res["Password"] == password:
                log.logger.info("Logged In")
                return "Logged In As Buyer"
            else:
                log.logger.info("Email Id and Password doesn't match")
                return "Email Id  and Password doesn't match"
        except Exception as E:
                print(E)



    def changing_password(self):
        """
        This method takes value from the dto class and sends the value to the database for updation
        :return: Updated if value is entered in the database
        """
        log.logger.info("In changing_password function of DaoUser layer")
        con = connect()
        ob_dto = change_password_dto.dto_forgot()
        (email, num, password) = ob_dto.get_values()
        mycol = con["Users"]
        find = mycol.find_one({"Email_Id": email})
        try:
            val = find['Phone Number']
            if val == num:
                try:
                    result = mycol.update_one({"Phone Number": num},{"$set": {"Password": password, "Confirm_Password": password}})
                    return "Updated"
                except Exception as e:
                    service = ServiceUser.ServiceImpl()
                    service.pymongo_exception()
            else:
                return "InvalidNumber"

        except TypeError as e:
            mycol_seller = con["Seller"]
            find2 = mycol_seller.find_one({"Email_Id": email})
            try:
                val = find2['Phone Number']
                if val == num:
                    try:
                        result = mycol_seller.update_one({"Phone Number": num}, {"$set": {"Password": password,"Confirm_Password": password}})
                        return "Updated"
                    except Exception as e:
                        service = ServiceUser.ServiceImpl()
                        service.pymongo_exception()
                else:
                    return "InvalidNumber"
            except TypeError as e:
                return "Invalid"




