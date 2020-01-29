from flask import Flask, escape, request, jsonify
from email_model import EmailModel
from email_service import EmailService

app = Flask(__name__)

@app.route('/')
def main():
    return jsonify(message = 'Only /email path is implemented'), 400

@app.route('/email', methods=["POST"])
def email():
    json_request = request.get_json(silent=True)
    if json_request == None:
        return jsonify(message = "No JSON request found"), 400

    email_service = EmailService()
    model = email_service.get_model_from_json(json_request)

    validation = email_service.validate_email(model)
    if(validation != True):
        return jsonify(message = validation)

    return 'All validation passes'

    # return email_service.send_email(test)