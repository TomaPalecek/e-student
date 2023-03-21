class SchoolYearExceptionName(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class SchoolYearNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
