"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from werkzeug.security import generate_password_hash, check_password_hash
from base64 import b64encode
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import cloudinary.uploader as uploader

api = Blueprint('api', __name__)

smtp_address = os.getenv("SMTP_ADDRESS")
smtp_port =  os.getenv("SMTP_PORT")
email_address =  os.getenv("EMAIL_ADDRESS")
email_password =  os.getenv("EMAIL_PASSWORD")

def set_password(password, salt):
    return generate_password_hash(f"{password}{salt}")


def check_password(hash_password, password, salt):
    return check_password_hash(hash_password, f"{password}{salt}")


# Allow CORS requests to this API
CORS(api)

def email_send(asunto, destinatario, body):
    message = MIMEMultipart("alternative")
    message["Subject"] = asunto
    message["From"] = email_address
    message["To"] = destinatario
    
    #Version HTML del body
    #''' indica principio y final de una cadena de texto
    html = '''
    
    <html>
    <body>
    <div>
    <p>
    Estás recibiendo este correo porque hiciste una solicitud de recuperación de contraseña para tu cuenta
    </p>
     ''' + body + '''   
    <p>
    Company Deimian
    </p>
    </div>
    </body>
    </html>
    '''

    #crear los elemento MIME
    html_mime = MIMEText(html, 'html')

    #adjuntamos el código html al mensaje
    message.attach(html_mime)

    #enviar el correo
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
            server.login(email_address, email_password)
            server.sendmail(email_address, destinatario, message.as_string())
        return True
    
    except Exception as error:
        print(str(error))
        return False



@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200



# @api.route("/sendemail", methods=["POST"])
# def send_email():
#     body = request.json
#     # result = email_send(body.get("subject"), body.get("to"), body.get("message"))
#     result = email_send(body.get("subject"), body.get("to"), body.get("message"))

#     if result == True:
#         return jsonify("se envio mensaje"), 200
    
#     else:
#         return jsonify("fallo mensaje"), 500


@api.route("/register", methods=["POST"])
def regiter_user():
    data_files = request.files
    data_form = request.form
    print(data_form)

    print(data_files)
    print(data_form)
    return jsonify("trabajando en ello"), 201
    # email = body.get("email")
    # password = body.get("password")
    # lastname = body.get("lastname")

    # if email is None or password is None:
    #     return jsonify({"message":"You need email and password"}), 400
    
    # user = User.query.filter_by(email=email).one_or_none()
    # if user is not None:
    #     return jsonify({"message":"the user exists"}), 400
    
    # else:
    #     salt = b64encode(os.urandom(32)).decode("utf-8")
    #     password = set_password(password, salt)
    #     user = User(email=email, password=password, salt=salt, lastname=lastname)
    #     db.session.add(user)

    #     try:
    #         db.session.commit()
    #         return jsonify({"message":"User created success"}), 201
    #     except Exception as error:
    #         db.session.rollback()
    #         return jsonify({"message":f"error: {error.args}"})



@api.route("/login", methods=["POST"])
def handle_login():
    body = request.json
    email = body.get("email")
    password = body.get("password")

    if email is None or password is None:
        return jsonify({"message":"You need email and password"}), 400
    else:
        user = User.query.filter_by(email=email).one_or_none()
        if user is None:
            return jsonify({"message":"Bad credentials"}), 400
        else:
            if check_password(user.password, password, user.salt):
                # le pasasmos un diccionario con lo necesario
                #OJO no se puede pasar informacion sencible por seguridad
                token = create_access_token(identity={
                    "user_id":user.id,
                    "rol":"general"
                })
                return jsonify({"token":token}), 200
            else:
                return jsonify({"message":"Bad credentials"}), 400
            

@api.route("/reset-password", methods=["POST"])
def reset_password():
    body = request.json

    result =email_send("reset password", body, "ingresa a este link para recuperar la contraseña hola https://ominous-yodel-v5p54wg6w2qrg-3000.app.github.dev/")

    if result == True:
        return jsonify("se envio mensaje"), 200
    
    else:
        return jsonify("fallo mensaje"), 500
