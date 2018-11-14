from unittest import TestCase
from Service import ServiceUser

class TestService(TestCase):
    def test_signup_detail_buyer(self):
        service = ServiceUser.ServiceImpl()
        request_data = {
         "Role":"Buyer",
        "Username":"Abc",
        "Age":"22",
        "Email_Id":"abc@gmail.com",
        "Password":"Abc@1234",
        "Confirm_Password":"Abc@1234",
        "Phone Number":"7077100197",
        "Address":"Bhubaneswar"

        }
        self.assertEqual(service.signup_detail(request_data),"Successfully added")

    def test_signup_detail_seller(self):
        service = ServiceUser.ServiceImpl()
        request_data = {
        "Role":"Seller",
        "Username":"Xyz",
        "Age":"22",
        "Email_Id":"xyz@gmail.com",
        "Password":"Xyz@1234",
        "Confirm_Password":"Xyz@1234",
        "Phone Number":"7077100938",
        "Address":"Bhubaneswar",
        "Aadhar":"12345678909"
        }
        self.assertEqual(service.signup_detail(request_data),"Successfully added")


    def test_login_details_emailid_buyer(self):
        service = ServiceUser.ServiceImpl()
        email_id = "xyz@gmail.com"
        password = "Xyz@1234"
        self.assertEqual(service.login_details_emailid(email_id,password),"Logged In As Buyer")

    def test_login_details_emailid_seller(self):
        service = ServiceUser.ServiceImpl()
        email_id = "xyz@gmail.com"
        password = "Xyz@1234"
        self.assertEqual(service.login_details_emailid(email_id,password),"Logged In As Seller")

    def test_changing_password(self):
        service = ServiceUser.ServiceImpl()
        email_id = ""
        password = ""
        num = ""
        self.assertEqual(service.changing_password( email_id,password,num),"Updated")

