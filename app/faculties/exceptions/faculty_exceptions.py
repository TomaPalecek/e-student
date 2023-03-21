class FacultyExceptionCode(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class FacultyNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
