"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
import smtplib
import os

api = Blueprint('api', __name__)

smtp_address = os.getenv("SMTP_ADDRESS")
smtp_port =  os.getenv("SMTP_PORT")
email_address =  os.getenv("EMAIL_ADDRESS")
email_password =  os.getenv("EMAIL_PASSWORD")


# Allow CORS requests to this API
CORS(api)

def email_send(subject, recipient, message):
    message = f"Subject: {subject}\nFrom: {recipient}\nTo: {recipient}\n{message}"
    try:
        server = smtplib.SMTP(smtp_address, smtp_port)
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail("ropamera@gmail.com", recipient, message)
        server.quit()
        print("se envio el mensaje")
        return True

    except Exception as error:
        print(error)
        print("Entre en el capturador de errores")
        return False



@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200



@api.route("/sendemail", methods=["POST"])
def send_email():
    body = request.json
    result = email_send(body.get("subject"), body.get("to"), body.get("message"))

    if result == True:
        return jsonify("se envio mensaje"), 200
    
    else:
        return jsonify("fallo mensaje"), 500


