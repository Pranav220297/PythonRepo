class InvalidUserError(Exception):
    def __init__(self, message, userid):
        super().__init__(message)
        self.message = message
        self.userid = userid