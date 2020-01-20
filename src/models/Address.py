from .ReadableFields import ReadableFields

class Address(ReadableFields):
    def __init__(self, street, number, neighboorhood, city, state, country, zip_code, nome_do_joao):
        self.street = street
        self.number = number
        self.neighboorhood = neighboorhood
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code
        self.nome_do_joao = nome_do_joao

