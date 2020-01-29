from flask import Flask, escape, request, jsonify
from email_model import EmailModel
from email_service import EmailService

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify(message = 'Only /email path is implemented'), 400

@app.route('/email')
def email():
    email_service = EmailService()

    test = EmailModel()
    test.to_addr = 'test@test.com'
    test.subject = 'test'
    test.body = 'test'

    return email_service.send_email(test)