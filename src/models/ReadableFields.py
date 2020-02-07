import copy
import ast

class ReadableFields:
    """
    This class is responsible for getting all fields from the constructors of 
    the classes that inherity from it
    """
    def __init__(self):
        """
        This constructor makes impossible to create a class without a __init__ mehtod.
        """
        raise Exception("Class must implement a constructor")
    
    def get_dict(self):
        """
        Return a copy of the dictionary that represents the class
        """
        return copy.deepcopy(self.__dict__)
    
    def get_deep_dict(self):
        """
        Return a dictionary represeting the classes and all their sub-classes
        """
        result = self.get_dict()
        mutiple_types = (list, tuple)
        default_types = (str,)
        for field in self.get_init_attributes():
            field_type = type(result[field])
            if field_type in mutiple_types:
                field_list = []
                for sub_field in field:
                    field_list.append(sub_field.get_deep_dict())
                result[field] = field_list
            elif not field_type in default_types:
                result[field] = result[field].get_deep_dict()
        return result

    @classmethod
    def get_init_attributes(cls):
        """
        Return a list of attributes of the class (excluding self and cls)
        """
        removable_attributes = ('self', 'cls')
        attributes = list(cls.__init__.__code__.co_varnames)
        for attribute in removable_attributes:
            try:
                attributes.remove(attribute)
            except ValueError:
                pass
        return attributes

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
    
    @classmethod
    def get_callable_classes(cls):
        """
        Return the a dictionary that represent fields and their respective class
        """
        from models import variables
        return variables

