
def copy_dict_to_object(dictionary: dict, data_object: object):
    if dictionary and data_object:
        for dict_key in dictionary:
            value = dictionary[dict_key]
            if hasattr(data_object, dict_key):
                setattr(data_object, dict_key, value)
    return data_object
