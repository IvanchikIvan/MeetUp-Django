class DatabaseError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class CriticalError(Exception):
    def __init__(self, message=""):
        super().__init__(message)
