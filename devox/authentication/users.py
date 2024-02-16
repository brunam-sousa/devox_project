class User:
    #array with ficticional users params (to tests)
    is_active = True
    username = 'bruna'
    password = 'teste'
    id = 1
    
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return self.is_active

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError("No `id` attribute - override `get_id`") from None