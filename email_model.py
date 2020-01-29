class EmailModel():
    to_addr: str #Kept consistent with required change to 'from' (see below)
    to_name: str
    from_addr: str #From is a reserved keyword in Python
    from_name: str 
    subject: str
    body: str