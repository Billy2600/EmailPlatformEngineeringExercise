from email_model import EmailModel
import jsonpickle

class EmailService():
    def send_email(self, email: EmailModel):
        return jsonpickle.encode(email, make_refs=False)