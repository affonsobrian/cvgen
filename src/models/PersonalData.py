from .Address import Address
from .ReadableFields import ReadableFields

class PersonalData(ReadableFields):
    """
    Information about personal data, such as name, address, relationship, objective, etc.
    """
    def __init__(self, name: str, address: Address, objective: str, relationship: str):
        self.name = name
        self.address = address
        self.objective = objective
        self.relationship = relationship
