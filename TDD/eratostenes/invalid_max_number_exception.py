class InvalidMaxNumberException(Exception):

    def __init__(self):
        Exception.__init__(self, "Max number must be greater than 2")
