from email_model import EmailModel
import requests
import json

class EmailService():
    def get_model_from_json(self, email_json):
        email_model = EmailModel()
        #Slight differences in naming between model and json we take in
        try:
            email_model.to_addr = email_json["to"]
        except KeyError: # We'll be doing validation later, just prevent a 500 error for now
            email_model.to_addr = ''

        try:
            email_model.to_name = email_json["to_name"]
        except KeyError:
            email_model.to_name = ''

        try:
            email_model.from_addr = email_json["from"]
        except KeyError:
            email_model.from_addr = ''

        try:
            email_model.from_name = email_json["from_name"]
        except KeyError:
            email_model.from_name = ''
        
        try:
            email_model.subject = email_json["subject"]
        except KeyError:
            email_model.subject = ''
        
        try:
            email_model.body = email_json["body"]
        except KeyError:
            email_model.body = ''

        return email_model


    # Returns error string or True if successful
    def validate_email(self, email: EmailModel):

        # Might be some refleciton/looping we could do here?
        if(not email.to_addr):
            return "'to' not set" #Return json name for this property, not model name
        if(not email.to_name):
            return "'to_name' not set"
        if(not email.from_addr):
            return "'from' not set"
        if(not email.from_name):
            return "'from_name' not set'"
        if(not email.subject):
            return "'subject' not set"
        if(not email.body):
            return "'body' not set"

        return True


    def send_email(self, email: EmailModel):
        return self.send_email_mailgun(email)

        # mailgun = False
        # sendgrid = False

        # mailgun = self.send_email_mailgun(email)
        
        # if(mailgun == False):
        #     sendgrid = self.send_email_sendgrid(email)

        # if(mailgun == True or sendgrid == True):
        #     return True
        # else:
        #     return False

    def send_email_mailgun(self, email: EmailModel):
        config = self.load_config()
        url = f'https://api:{config["mailgun_api_key"]}@{config["mailgun_base_addr"]}/{config["mailgun_domain_name"]}/messages'
        payload = {
            "from": f'{email.from_name} <{email.from_addr}>',
            "to": f'{email.to_name} <{email.to_addr}>',
            "subject": email.subject,
            "text": email.body
        }
        r = requests.post(url = url, data = payload)
        if(r.status_code == requests.codes.ok):
            return True
        else:
            return False

    def send_email_sendgrid(self, email: EmailModel):
        config = self.load_config()
        url = config["sendgrid_url"]
        headers = { 'Authorization': f'Bearer {config["sendgrid_auth_token"]}' }
        payload = {"personalizations":
            [{"to": [{"email": email.to_addr, "name": email.to_name}]}],
            "from": {"email": email.from_addr, "name": email.from_name},
            "subject": email.subject,
            "content": [{
                "type": "text/plain", "value": email.body
            }]
        }
        r = requests.post(url = url, json = payload, headers = headers)
        if(r.status_code == requests.codes.accepted):
            return True
        else:
            return False

    # In a 'real' project this would likely be its own class
    def load_config(self):
        with open('config.json') as config:
            data = json.load(config)

        return data