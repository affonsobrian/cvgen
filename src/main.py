from models.Curriculum import Curriculum
from models.PersonalData import PersonalData

instance = Curriculum.generate_instance()

print(instance.get_deep_dict())