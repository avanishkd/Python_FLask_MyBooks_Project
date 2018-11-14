from flask import jsonify,request,Blueprint #importing flask, jsonify the object, request
from Service import ServiceAdmin #importing service layer


admin_page = Blueprint('admin_page', __name__, template_folder='templates')


@admin_page.route('/addbook',methods=['POST'])
def admin_add_books():
    '''
    adding the book details-isbn, publisher, author, price, type, define
    :return:reponse
    '''
    request_data = request.get_json()
    service = ServiceAdmin.Service_impl_admin()
    response = service.add_books(request_data)
    return jsonify(response)


@admin_page.route('/delbook',methods=['POST'])
def admin_del_books():
    '''
    deleting the specific books
    :return: reponse
    '''
    request_data = request.get_json()
    service = ServiceAdmin.Service_impl_admin()
    response = service.delete_books(request_data)
    return jsonify(response)
