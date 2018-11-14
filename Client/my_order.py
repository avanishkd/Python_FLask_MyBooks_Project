from flask import jsonify,request,Blueprint #importing flask, jsonify the object, request
from Service import ServiceOrder #importing service layer


order_page = Blueprint('order_page', __name__, template_folder='templates')


@order_page.route('/add_to_wishlist',methods=['POST'])
def to_wishlist():
    '''
        This controller method (API) maps with the front end of the application,
         it will receive the request and will send it to the business layer for further proccesing
        :return: The methods return Updated response or returns correct error message
    '''
    service = ServiceOrder.Service_Order()
    request_data = request.get_json()
    result = service.add_to_wishlist(request_data)
    return jsonify(result)


@order_page.route('/display_wishlist',methods=['GET'])
def display_wishlist():
    '''
        This controller method (API) maps with the front end of the application,
        it will receive the request and will send it to the business layer for further proccesing
        :return: The methods return list of books in the wishlist of a particular buyer or returns correct error message
    '''
    service = ServiceOrder.Service_Order()
    result = service.display_wishlist_service()
    return jsonify(result)


@order_page.route('/add_to_cart',methods=['POST'])
def to_cart():
    """
        This controller method (API) maps with the front end of the application,
        it will receive the request and will send it to the business layer for further proccesing
        :return: The methods return response success message or error message
    """
    service = ServiceOrder.Service_Order()
    request_data = request.get_json()
    result = service.add_to_cart_service(request_data)
    return jsonify(result)


@order_page.route('/display_books',methods=['POST'])
def display():
    """
        This controller method (API) maps with the front end of the application,
        it will receive the request and will send it to the business layer for further proccesing
        :return:This method would display the details of the book and the details of the sellers selling that particular book
    """
    service = ServiceOrder.Service_Order()
    request_data = request.get_json()
    result = service.display_details(request_data)
    return jsonify(result)


@order_page.route('/order_books',methods=['POST'])
def order():
    """
        This controller method (API) maps with the front end of the application,
        it will receive the request and will send it to the business layer for further proccesing
        :return: The methods return ordered response or returns correct error message
    """
    service = ServiceOrder.Service_Order()
    request_data = request.get_json()
    result = service.order_book_service(request_data)
    return jsonify(result)



