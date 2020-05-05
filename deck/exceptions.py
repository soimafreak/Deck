"""Exceptions module."""

class NotASuite(Exception):
    """Exception class for When it's not a Suite errors."""

    pass

class NumberOutsideOfRange(Exception):
    """Exception class for When Number is out of range errors."""

    pass

class NotADeck(Exception):
    """Exception class for When invalide deck type requested errors."""

    pass
