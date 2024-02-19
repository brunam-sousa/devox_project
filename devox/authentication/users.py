from flask_login import UserMixin

class User(UserMixin):
#    def __init__(self):
        # mock database 
        id = '1'
        name = 'bruna'
        password = 'teste'