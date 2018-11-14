from flask import jsonify,request,Blueprint #importing flask, jsonify the object, request
from Service import ServiceSeller#importing service layer


seller_page = Blueprint('seller_page', __name__, template_folder='templates')


@seller_page.route('/show_books',methods=['POST'])
def show_books():
    '''
       displaying books to the customer
       :return:list of books in the book database
    '''
    request_data = request.get_json()
    service = ServiceSeller.Service_impl_Seller()
    result = service.show_books(request_data)
    return jsonify(result)


@seller_page.route('/seller_add_books',methods=['PATCH'])
def seller_add_books():
    '''
        adding books to the seller database by getting request from admin
        :return:response
    '''
    request_data = request.get_json()
    service = ServiceSeller.Service_impl_Seller()
    result = service.seller_add_books(request_data)
    return jsonify(result)


@seller_page.route('/seller_update_books',methods=['PATCH'])
def seller_update_books():
    '''
        updating books in the seller database
        :return:response
    '''
    request_data = request.get_json()
    service = ServiceSeller.Service_impl_Seller()
    result = service.seller_update_books(request_data)
    return jsonify(result)

