from datetime import date

from .Address import Address
from .ReadableFields import ReadableFields

class ProfessionalExperience(ReadableFields):
    """
    Storage information about a specific professional experience.
    """
    def __init__(self, start: date, end: date, company: str, description: str, city: str, country: str):
        self.start = start
        self.end = end
        self.company = company
        self.description = description
        self.city = city
        self.country = country
