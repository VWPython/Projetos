class InvalidMaxNumberException(Exception):
    """
    Thrown an exception if the max number is greater than 2
    """

    def __init__(self):
        Exception.__init__(self, "Max number must be greater than 2")
