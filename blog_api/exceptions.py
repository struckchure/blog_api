class Exception(Exception):

    message = "An Error Occured"

    def __init__(self, message=None):
        self.message = message or self.message or self.__doc__

    def __str__(self):
        if isinstance(self.message, str):
            return self.message
        return ""

    def __dict__(self):
        if isinstance(self.message, dict):
            return self.message
        return {}
