from flask import Flask,jsonify,request #importing flask, jsonify the object, request
from flask_cors import CORS,cross_origin #importing cross origin
from Service import ServiceUser,ServiceUpdate#importing service layer
from Client.mybook_admin import admin_page#importing Client admin layer
from Client.my_order import order_page#importing Client order layer
from Client.mybook_seller import seller_page#importing Client Seller layer




app=Flask(__name__)
app.register_blueprint(admin_page)
app.register_blueprint(order_page)
app.register_blueprint(seller_page)
CORS(app)


@cross_origin("*")
@app.route('/signup', methods=['POST'])#localhost api name: /signup, method = POST
def user_signup():
  '''
  extracting user sign up detail from client side (web page)
  :return: response from the database in json format
  '''
  request_data = request.get_json()
  service = ServiceUser.ServiceImpl()
  response = service.signup_detail(request_data)
  return jsonify(response),201

@app.route('/hello',methods=['GET'])
def display_hello():
    """
    Get method to display HELLO WORLD
    """
    str = "HELLO WORLD"
    return jsonify(str)


@app.route('/login_emailid', methods=['POST'])  # localhost api name: /login_emailid , method=POST
def user_login_emailid():
    '''
            extracting user login details from client side (web page)
            :return: response from database in json format
            '''
    request_data = request.get_json()
    service = ServiceUser.ServiceImpl()
    email_id = request_data['Email_Id']
    password = request_data['Password']
    response = service.login_details_emailid(email_id, password)
    return jsonify(response), 202



@app.route('/change_password', methods=['POST'])
def change_password():
    '''
    This controller method (API) maps with the front end of the application,
     it will receive the request and will send it to the buisness layer for further proccesing
    :return: The methods return Updated when password is updated successfully or returns correct error message
    '''

    service = ServiceUser.ServiceImpl()
    val = request.get_json()
    uemail = val['Email_Id']
    uname = val['Phone Number']
    npword = val['Password']
    res = service.changing_password(uemail,uname,npword)
    return jsonify(res),201




@app.route('/update_email',methods=['PATCH'])
def update_email():
    """
        This controller method (API) maps with the front end of the application,
         it will receive the request and will send it to the buisness layer for further proccesing
        :return: The methods return Updated response or returns correct error message
    """
    service = ServiceUpdate.Service_Update()
    request_data = request.get_json()
    result = service.update_email(request_data)
    return jsonify(result),201



@app.route('/update_number',methods=['PATCH'])
def update_number():
    """
        This controller method (API) maps with the front end of the application,
         it will receive the request and will send it to the buisness layer for further proccesing
        :return: The methods return Updated response or returns correct error message
    """
    service = ServiceUpdate.Service_Update()
    request_data = request.get_json()
    result = service.update_phone(request_data)
    return jsonify(result),201


@app.route('/update_address',methods=['PATCH'])
def update_address():
    """
        This controller method (API) maps with the front end of the application,
         it will receive the request and will send it to the buisness layer for further proccesing
        :return: The methods return Updated response or returns correct error message
    """
    service = ServiceUpdate.Service_Update()
    request_data = request.get_json()
    result = service.update_address_service(request_data)
    return result,201


@app.route('/update_password',methods=['PATCH'])
def update_password():
    """
        This controller method (API) maps with the front end of the application,
         it will receive the request and will send it to the buisness layer for further proccesing
        :return: The methods return Updated response or returns correct error message
    """
    service = ServiceUpdate.Service_Update()
    request_data = request.get_json()
    result = service.update_password_service(request_data)
    return jsonify(result),201


@app.route('/display_homepage',methods=['GET'])
def display_books():
    """
    This method displays the books present in the database to the front end
    :return: List containing details of all the books present in the database
    """
    service = ServiceUpdate.Service_Update()
    result = service.display_service()
    return jsonify(result),201


app.run(port=8085,debug="True")

