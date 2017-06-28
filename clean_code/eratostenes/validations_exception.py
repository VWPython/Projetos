class InvalidInsertedNumberException(Exception):
    """
    Thrown an exception if the inserted number is a integer and greater than 2
    """

    def __init__(self):
        Exception.__init__(self, "Inserted number must be integer and greater than 2")
