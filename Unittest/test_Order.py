from unittest import TestCase
from Service import ServiceOrder
from DTO import login_dto

class TestService(TestCase):
    def test_add_to_wishlist(self):
        service = ServiceOrder.Service_Order()
        user_id =""
        password = ""
        login_dto.login_dto.set_values(self,user_id,password)
        request_data = {"ISBN":""}
        self.assertEqual(service.add_to_wishlist(request_data), "Added to wishlist successfully")