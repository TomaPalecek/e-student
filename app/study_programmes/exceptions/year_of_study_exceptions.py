class YearOfStudyNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class YearOfStudyOutOfBoundsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class YearOfStudyExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
