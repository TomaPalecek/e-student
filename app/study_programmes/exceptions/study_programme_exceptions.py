class StudyProgrammeExistsException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class StudyProgrammeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
