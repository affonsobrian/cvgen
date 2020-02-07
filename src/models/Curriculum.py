from .PersonalData import PersonalData
from .ReadableFields import ReadableFields

class Curriculum(ReadableFields):
    """
    Class responsible for storing all the data into an object, able to render the template.
    """
    def __init__(self, personal_data: PersonalData, professionl_experiences: list):
        self.personal_data = personal_data
        self.professionl_experiences = professionl_experiences

    @classmethod
    def generate_instance(cls):
        """
        Generate a instance of the class by receiving it fields automatically on the terminal
        """
        kwargs = {}
        callable_classes = cls.get_callable_classes()
        for field in cls.get_init_attributes():
            if field in callable_classes.keys():
                kwargs[field] = callable_classes[field].generate_instance()
            else:
                kwargs[field] = input(f"Please inform {field}: ")
        return cls(**kwargs)

